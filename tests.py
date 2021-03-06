##################################################
#
#   Author          : josuebrunel
#   Filename        : tests.py
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Tue 19 May 2015 01:46:25 PM CEST
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
        cmd="python myql-cli.py run {0} {1}".format(args, query)
        logger.debug(cmd)
        exit_code = subprocess.call("{0}".format(cmd), shell=True)
        return exit_code

    def testXML(self,):
        logger.debug(__name__)
        self.assertEquals(self.execute('--format xml'),0)
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


class TestYqlOAuth(unittest.TestCase):

    def execute(self, *args):
        cmd="python myql-cli.py run {0} '{1}'".format(*args)
        logger.debug(cmd)
        exit_code = subprocess.call("{0}".format(cmd), shell=True)
        return exit_code

    def testGUID(self,):

        self.assertEquals(self.execute('--format json','select * from yahoo.identity where yid="spullara"'),0)

class TestYqlTable(unittest.TestCase):

    def execute(self, args):
        project='congoyql'
        cmd = "python myql-cli.py table {0} {1}".format(args, project)
        logger.debug(cmd)
        exit_code = subprocess.call("{0}".format(cmd), shell=True)
        return exit_code

    def testInit(self,):
        self.assertEquals(self.execute('--init'),0)

    def testCreate(self,):
        self.assertEquals(self.execute('--create'),0)

class TestYqlConfig(unittest.TestCase):

    def execute(self, args):
        cmd = "python myql-cli.py init-config {0}".format(args)
        exit_code = subprocess.call("{0}".format(cmd), shell=True)
        return exit_code

    def testCreateConfigFile(self):
        logger.debug(__name__)
        config_file=os.path.join(os.path.expanduser('~'),'.myql-cli.ini')
        try:
            logger.debug("Trying to delete {0}".format(config_file))
            os.remove(config_file)
        except:
            pass

        self.assertEquals(self.execute(''),0)
        self.assertEquals(os.path.isfile(config_file),True)
