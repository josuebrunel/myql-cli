##################################################
#
#   Author          : josuebrunel
#   Filename        : yql-cli.py
#   Description     :
#   Creation Date   : 02-04-2015
#   Last Modified   : Thu 02 Apr 2015 05:57:27 PM CEST
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
        
        yql = LokingYQL(community=True)

        response = yql.rawQuery(value)

        if not response.status_code == 200:
            print(response.content)
            sys.exit(1)

        print(response.json())
        sys.exit(0)

class ShellAction(argparse.Action):

    def __call__(self, parser, namespace, value, option_string=None):
        pass

class TableAction(argparse.Action):

    def __call__(self, parser, namespace, value, option_string=None):
        pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser("YQL-cli tools")

    parser.add_argument(
        '-c',
        '--command',
        action=ExecuteAction,
        help="Execute an YQL query"
    )

    parser.add_argument(
        'shell',
        action=ShellAction,
        help="SQL like shell"
    )

    parser.add_argument(
        'create-table',
        action=TableAction,
        help="Create a YQL Table from python file"
    )

    args = vars(parser.parse_args())
