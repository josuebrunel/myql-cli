import os, sys
import cmd
import argparse
import importlib

from utils import pretty_xml, pretty_json
from utils import create_init_file, create_tables_file, create_directory

from myql import MYQL
from myql.contrib.table import TableMeta

__author__  = 'josue kouka'
__email__   = 'josuebrunel@gmail.com'
__version__ = '0.2.3'


########################################################
#
#           COMMAND LINE QUERIES HANDLER
#
########################################################

class ExecuteAction(argparse.Action):
    '''Action performed for Execute command
    '''
    def __call__(self, parser, namespace, value, option_string=None):

        attr = {
            'community': True,
            'format': namespace.format,
            'jsonCompact': namespace.jsonCompact,
            'debug': namespace.debug,
        }

        yql = MYQL(**attr)
        yql.diagnostics = namespace.diagnostics

        response = yql.rawQuery(value)

        if not response.status_code == 200:
            print(response.content)
            sys.exit(1)

        if namespace.format == 'json':
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

        if namespace.create :
            module_name = value
            module = importlib.import_module(module_name)
            tables = [ v for k,v in module.__dict__.items() if isinstance(v, TableMeta) and k != 'TableModel']

            for table in tables :
                table_name = table.table.name
                path= os.path.realpath(value)
                table.table.save(name=table_name, path=path)

            sys.exit(0)

        if namespace.init :
            folder = value  
            if not create_directory(folder):
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
        default='json',
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
        help="Creates a tables.py file with sample in it"
    )
    table_parser.add_argument(
        '-c',
        '--create',
        action='store_true',
        help="Creates tables in the tables.py file"
    )

    table_parser.add_argument(
        '-p',
        '--path',
        action='store',
        help="Location of the xml table file to create"
    )
    
    args = vars(parser.parse_args())
    print args

