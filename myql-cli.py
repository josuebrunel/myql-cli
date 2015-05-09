#!/usr/bin/env python

import os, sys
import cmd
import argparse
import importlib

from utils import pretty_xml, pretty_json
from utils import create_init_file, create_tables_file, create_directory, get_module
from utils import create_config_file, read_config_file, config_file_exists

from myql import MYQL
from myql.contrib.table import TableMeta
from myql.contrib.auth import YOAuth

__author__  = 'josue kouka'
__email__   = 'josuebrunel@gmail.com'
__version__ = '0.2.3'


########################################################
#
#           CONFIG FILE HANDLER
#
########################################################

class ConfigAction(argparse.Action):
    '''Action performed for Init command
    '''

    def __call__(self, parser, namespace, value, option_string=None):
        if not config_file_exists():
            create_config_file()
            sys.exit(0)

        print("Config file already exists")
        sys.exit(1)

########################################################
#
#           COMMAND LINE QUERIES HANDLER
#
########################################################

class ExecuteAction(argparse.Action):
    '''Action performed for Execute command
    '''
    def __call__(self, parser, namespace, value, option_string=None):

        config = read_config_file()
        
        format =  namespace.format if namespace.format else config.get('DEFAULT','format')
        oauth = config.getboolean('DEFAULT','oauth')

        # Checking ig OAuth params are defined
        if oauth :
            oauth = YOAuth(None, None, from_file=config.get('auth','from_file'))

        attr = {
            'community': True,
            'format': format,
            #'jsonCompact': namespace.jsonCompact if namespace.jsonCompact else config.getboolean(format, 'jsonCompact'),
            'debug': namespace.debug if namespace.debug else config.getboolean(format, 'debug'),
            'oauth': oauth
        }

        
        yql = MYQL(**attr)
        yql.diagnostics = namespace.diagnostics if namespace.diagnostics else config.getboolean(format, 'diagnostics')

        response = yql.rawQuery(value)

        if not response.status_code == 200:
            print(response.content)
            sys.exit(1)

        if format == 'json':
            print(pretty_json(response.content))
        else:
            print(pretty_xml(response.content))
        sys.exit(0)

############################################################
#
#                   SHELL QUERIES HANDLER
#
############################################################

class ShellAction(argparse.Action):
    '''Action performed for shell command
    '''
    def __call__(self, parser, namespace, value, option_string=None):
        pass

class ShellCmd(cmd.Cmd):
    pass
############################################################
#
#                   YQL TABLE HANDLER
#
###########################################################

class TableAction(argparse.Action):
    '''Action performed for Table command
    '''
    def __call__(self, parser, namespace, value, option_string=None):

        if namespace.init and namespace.create:
            print("Optional arguments --init and --create can't be used together")
            sys.exit(1)

        # Case where non argument is given
        if not namespace.init and not namespace.create:
            namespace.create = True

        if namespace.create :
            if not os.path.isdir(os.path.realpath(value)):
                print("{0} table project doesn't exist yet. \n \tpython myql-cli table -i {0} ".format(value))
                sys.exit(1)

            module_path = os.path.realpath(value)
            module = get_module(module_path)
            tables = [ v for k,v in module.__dict__.items() if isinstance(v, TableMeta) and k != 'TableModel']

            for table in tables :
                table_name = table.table.name
                path= os.path.realpath(value)
                table.table.save(name=table_name, path=path)

            sys.exit(0)

        if namespace.init :
            folder = value  
            if not create_directory(folder):
                print("This project already exists !!!")
                sys.exit(0)

            create_init_file(folder)
            create_tables_file(folder)

            sys.exit(0)

        sys.exit(1)

############################################################
#
#                           MAIN
#
############################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser("YQL-cli tools", version=__version__)

    subparsers = parser.add_subparsers(help='commands')

    # CONFIG
    config_parser = subparsers.add_parser('init-config', help='Init a config file .myql-cli.ini in your home directory')
    config_parser.add_argument('init-config', action=ConfigAction, default=True, nargs='*', help='Config File Management')


    # EXECUTE QUERY
    execute_parser = subparsers.add_parser('execute', help='Executes a YQL query')
    execute_parser.add_argument(
        'execute',
        action=ExecuteAction,
        help="Execute a YQL query"
    )
    execute_parser.add_argument(
        '--format',
        action='store',
        #default='json',
        choices=('json','xml'),
        help="Response returned format"
    )
    execute_parser.add_argument(
        '--pretty',
        action='store_true',
        default=False,
        help="Response returned format prettyfied"
    ) 
    execute_parser.add_argument(
        '--jsonCompact',
        action='store_true',
        default=False,
        help="Json response compacted"
    )
    execute_parser.add_argument(
        '--diagnostics',
        action='store_true',
        default=False,
        help="Response with diagnostics"
    )   
    execute_parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help="Response with diagnostics"
    )
    execute_parser.add_argument(
        '--oauth',
        action='store',
        help="OAuth credentials"
    )
    # LAUNCH SHELL
    shell_parser = subparsers.add_parser('shell', help='Prompts a YQL shell command')
    shell_parser.add_argument(
        'shell',
        action=ShellAction,
        help="SQL like shell"
    )

    # CREATE YQL TABLE
    table_parser = subparsers.add_parser('table', help='Creates a YQL table')
    table_parser.add_argument(
        'table',
        action=TableAction,
        help="Create a YQL Table from python file"
    )
    table_parser.add_argument(
        '-i',
        '--init',
        action='store_true',
        help="Creates a project with an tables.py file in it"
    )
    table_parser.add_argument(
        '-c',
        '--create',
        action='store_true',
        help="Creates tables in the tables.py file of your project"
    )

    args = vars(parser.parse_args())

