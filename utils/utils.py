import os
import json
from xml.dom import minidom
from xml.etree import cElementTree as ctree

def pretty_xml(data):
    parsed_string = minidom.parseString(data)
    return parsed_string.toprettyxml(indent="\t")

def pretty_json(data):
    data = json.loads(data)
    return json.dumps(data, indent=4, sort_keys=False)

def create_directory(path=None):
    dir = os.path.realpath(path if path else '.')
    if os.path.isdir(dir):
        print("This project already exists !!!")
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
    data = "from myql.contrib.table import TableModel, BinderModel, BinderKey, BinderPage\n \nclass YourBinder(BinderModel):\n \t #Your code \n \nclass YourTable(TableModel):\n \t #Your code\n"
    create_file('tables',data,path)
    return True
        
