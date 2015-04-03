##################################################
#
#   Author          : josuebrunel
#   Filename        : yql-cli.py
#   Description     :
#   Creation Date   : 02-04-2015
#   Last Modified   : Fri 03 Apr 2015 03:09:55 PM UTC
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

        print(namespace)

        attr = {
            'community': True,
            'format': namespace.format,
            'jsonCompact': namespace.jsonCompact,
        }

        #yql = LokingYQL(format=format, community=True)
        yql = LokingYQL(**attr)

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
    # LAUNCH SHELL
    shell_parser = subparsers.add_parser('shell', help='Prompt a shell')
    shell_parser.add_argument(
        'shell',
        action=ShellAction,
        help="SQL like shell"
    )

    # CREATE YQL TABLE
    create_parser = subparsers.add_parser('create-table', help='Create a YQL table')
    create_parser.add_argument(
        'create-table',
        action=TableAction,
        help="Create a YQL Table from python file"
    )
    create_parser.add_argument(
        '--path',
        action='store',
        help="Location of the xml table file to create"
    )
    
    args = vars(parser.parse_args())
    print args

