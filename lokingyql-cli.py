##################################################
#
#   Author          : josuebrunel
#   Filename        : yql-cli.py
#   Description     :
#   Creation Date   : 02-04-2015
#   Last Modified   : Thu 02 Apr 2015 05:03:00 PM CEST
#
##################################################

import pdb
import argparse

class ExecuteAction(argparse.Action):

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

    args = vars(parser.parse_args())
