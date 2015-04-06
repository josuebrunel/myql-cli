##################################################
#
#   Author          : josuebrunel
#   Filename        : tests.py
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Mon 06 Apr 2015 05:00:51 AM CEST
#
##################################################

import os, logging
import unittest
import subprocess

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logger = logging.getLogger(__name__)



class TestYqlQuery(unittest.TestCase):
    

    def execute(self, args):
        query="'select * from geo.countries where name=\"Congo\"'"
        cmd="python myql-cli.py execute {0} {1}".format(args, query)
        logger.debug(cmd)
        exit_code = subprocess.call("{0}".format(cmd), shell=True)
        return exit_code

    def testJsonCompact(self,):
        logger.debug(__name__)
        self.assertEquals(self.execute('--format json --jsonCompact'),0)

    def testDiagnostics(self,):
        logger.debug(__name__)
        self.assertEquals(self.execute('--diagnostics'),0)

    def testDebug(self,):
        logger.debug(__name__)
        self.assertEquals(self.execute('--debug'),0)

    def testAllOptions(self,):
        logger.debug(__name__)
        self.assertEquals(self.execute('--format json --debug --diagnostics --jsonCompact'),0)
