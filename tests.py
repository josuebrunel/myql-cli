##################################################
#
#   Author          : josuebrunel
#   Filename        : tests.py
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Fri 03 Apr 2015 03:43:30 PM UTC
#
##################################################

import os
import unittest
import subprocess

class TestQueryShell(unittest.TestCase):

    def execute(self, args):
        query="'select * from geo.countries where name=\"Congo\"'"
        cmd="python lokingyql-cli.py execute {0} {1}".format(args, query)
        print(cmd)
        exit_code = subprocess.call("{0}".format(cmd), shell=True)
        return exit_code

    def testJsonCompact(self,):
        self.assertEquals(self.execute('--format json --jsonCompact'),0)
