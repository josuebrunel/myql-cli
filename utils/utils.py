import os
import imp
import json
import ConfigParser
from xml.dom import minidom
from xml.etree import cElementTree as ctree

CONFIG_FILE = os.path.join(os.path.expanduser('~'),'.myql-cli.ini')

def pretty_xml(data):
    parsed_string = minidom.parseString(data)
    return parsed_string.toprettyxml(indent="\t")

def pretty_json(data):
    data = json.loads(data)
    return json.dumps(data, indent=4, sort_keys=False)

def create_directory(path=None):
    dir = os.path.realpath(path if path else '.')
    if os.path.isdir(dir):
        return False

    os.mkdir(dir, 0755)
    return True

def create_file(fname, data, path=None):
    path = path if path else '.'
    ftables = os.path.realpath(os.path.join(path,fname+'.py'))
    with open(ftables, 'w') as f:
        f.write(data)
    return True

def create_init_file(path=None):
    data = "from tables import * \n \n"
    create_file('__init__', data, path)

def create_tables_file(path=None):
    data = "from myql.contrib.table import TableModel, BinderModel, BinderKey, BinderPage\n\nclass YourBinder(BinderModel):\n\t#Your code\n\tpass\nclass YourTable(TableModel):\n\t#Your code\n\tpass\n"
    create_file('tables',data,path)
    return True
        
def get_module(path):
    module = imp.load_package('module',path)
    return module

def config_file_exists():
    if os.path.isfile(CONFIG_FILE):
        return True
    return False

def create_config_file():
    config = ConfigParser.RawConfigParser()

    # default section
    #config.add_section('default_format')
    config.set('','format','json')
    config.set('','oauth',False)
    # json section
    config.add_section('json')
    config.set('json', 'diagnostics', False)
    config.set('json', 'debug', False)
    config.set('json', 'jsonCompact', False)
    # xml section 
    config.add_section('xml')
    config.set('xml', 'diagnostics', False)
    config.set('xml', 'debug', False)
    # oauth section
    config.add_section('auth')
    config.set('auth', 'from_file', None)
    
    with open(CONFIG_FILE, 'wb') as f:
        config.write(f)
    return True

def read_config_file():
    config = ConfigParser.RawConfigParser()
    if not config.read(CONFIG_FILE):
        print("No Config File Found")
        create_config_file()
        print("Config File Created")
        config.read(CONFIG_FILE)

    return config

