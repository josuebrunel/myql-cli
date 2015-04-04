##################################################
#
#   Author          : josuebrunel
#   Filename        : yql-cli.py
#   Description     :
#   Creation Date   : 02-04-2015
#   Last Modified   : Sat 04 Apr 2015 05:20:02 AM UTC
#
##################################################

__author__  = 'josue kouka'
__email__   = 'josuebrunel@gmail.com'
__version__ = '0.2.3'

import pdb
import sys
import cmd
import argparse

from lokingyql import LokingYQL

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
            #'diagnostics': namespace.diagnostics,
        }

        yql = LokingYQL(**attr)
        yql.diagnostics = namespace.diagnostics

        response = yql.rawQuery(value)

        if not response.status_code == 200:
            print(response.content)
            sys.exit(1)
        
        if format == 'json':
            print(response.json())
        else:
            print(response.content)
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
        pass

############################################################
#
#                           MAIN
#
############################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser("YQL-cli tools", version=__version__)

    subparsers = parser.add_subparsers(help='commands')

    # EXECUTE QUERY
    execute_parser = subparsers.add_parser('execute', help='Execute an YQL query')
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
    shell_parser = subparsers.add_parser('shell', help='Prompt a shell')
    shell_parser.add_argument(
        'shell',
        action=ShellAction,
        help="SQL like shell"
    )

    # CREATE YQL TABLE
    table_parser = subparsers.add_parser('table', help='Create a YQL table')
    table_parser.add_argument(
        'table',
        action=TableAction,
        help="Create a YQL Table from python file"
    )
    table_parser.add_argument(
        '--path',
        action='store',
        help="Location of the xml table file to create"
    )
    
    args = vars(parser.parse_args())
    print args

