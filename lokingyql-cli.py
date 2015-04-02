##################################################
#
#   Author          : josuebrunel
#   Filename        : yql-cli.py
#   Description     :
#   Creation Date   : 02-04-2015
#   Last Modified   : Thu 02 Apr 2015 09:04:33 PM UTC
#
##################################################

__author__  = 'josue kouka'
__email__   = 'josuebrunel@gmail.com'

import pdb
import sys
import cmd
import argparse

from lokingyql import LokingYQL

class ExecuteAction(argparse.Action):

    def __call__(self, parser, namespace, value, option_string=None):
       
        format = namespace.format

        yql = LokingYQL(format=format, community=True)

        response = yql.rawQuery(value)

        if not response.status_code == 200:
            print(response.content)
            sys.exit(1)
        
        if format == 'json':
            print(response.json())
        else:
            print(response.content)
        sys.exit(0)

class ShellAction(argparse.Action):

    def __call__(self, parser, namespace, value, option_string=None):
        pass

class TableAction(argparse.Action):

    def __call__(self, parser, namespace, value, option_string=None):
        pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser("YQL-cli tools")

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
    # LAUNCH SHELL
    shell_parser = subparsers.add_parser('shell', help='Prompt a shell')
    shell_parser.add_argument(
        'shell',
        action=ShellAction,
        help="SQL like shell"
    )

    # CREATE YQL TABLE
    create_parser = subparsers.add_parser('create', help='Create a YQL table')
    create_parser.add_argument(
        'create-table',
        action=TableAction,
        help="Create a YQL Table from python file"
    )
    
    args = vars(parser.parse_args())
    print args

