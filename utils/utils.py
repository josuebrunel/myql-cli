import json
from xml.dom import minidom
from xml.etree import cElementTree as ctree

def pretty_xml(data):
    parsed_string = minidom.parseString(data)
    return parsed_string.toprettyxml(indent="\t")

def pretty_json(data):
    data = json.loads(data)
    return json.dumps(data, indent=4, sort_keys=False)
