##################################################
#
#   Author          : josuebrunel
#   Filename        : tests.py
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Sun 05 Apr 2015 01:12:43 PM CEST
#
##################################################

import os, logging
import unittest
import subprocess

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(funcName)s] %(message)s \n")
logger = logging.getLogger(__name__)



class TestYqlQuery(unittest.TestCase):
    

    def execute(self, args):
        query="'select * from geo.countries where name=\"Congo\"'"
        cmd="python lokingyql-cli.py execute {0} {1}".format(args, query)
        logger.debug(cmd)
        print("\n")
        exit_code = subprocess.call("{0}".format(cmd), shell=True)
        return exit_code

    def testJsonCompact(self,):
        self.assertEquals(self.execute('--format json --jsonCompact'),0)

    def testDiagnostics(self,):
        self.assertEquals(self.execute('--diagnostics'),0)

    def testDebug(self,):
        self.assertEquals(self.execute('--debug'),0)

    def testAllOptions(self,):
        self.assertEquals(self.execute('--format json --debug --diagnostics --jsonCompact'),0)
