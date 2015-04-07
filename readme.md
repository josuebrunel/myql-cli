### MYQL-CLI

***MYQL-cli*** is a command line tool to make YQL queries through the command line

#### Installation

```shell
$ pip install myql # Not available yet
```

Or by downloading the package and performing

```shell
$ python setup.py install --record files.txt # the record just to help when uninstalling the tool
```

#### How To

```shell
usage: YQL-cli tools [-h] [-v] {execute,shell,table} ...

positional arguments:
  {execute,shell,table}
                        commands
    execute             Executes a YQL query
    shell               Prompts a YQL shell command
    table               Creates a YQL table

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program\'s version number and exit
```

##### Query Tool

```shell
$ myql-cli execute -h
usage: YQL-cli tools execute [-h] [--format {json,xml}] [--pretty]
                             [--jsonCompact] [--diagnostics] [--debug]
                             execute

positional arguments:
  execute              Execute a YQL query

optional arguments:
  -h, --help           show this help message and exit
  --format {json,xml}  Response returned format
  --jsonCompact        Json response compacted
  --diagnostics        Response with diagnostics
  --debug              Response with diagnostics
```

```shell
$ myql-cli execute --format json "select name from geo.states where place='Congo'"
```

##### YQL Shell

```shell
$ myql-cli shell -h
```

```shell
$ myql-cli shell
yql> 
```

##### Table Manager

```shell
$ myql-cli table -h
usage: YQL-cli tools table [-h] [-i] [-c] table

positional arguments:
  table         Create a YQL Table from python file

optional arguments:
  -h, --help    show this help message and exit
  -i, --init    Creates a project with an tables.py file in it
  -c, --create  Creates tables in the tables.py file of your project
```

* Initialize the table project

```shell
$ myql-cli table -i lol
$ ls -l lol
__init__.py tables.py
```

* Define your table

```python
from myql.contrib.table import BinderModel, BinderKey, BinderPage, TableModel

class SelectBinder(BinderModel):
    name = 'select'
    itemPath = 'products.product'
    produces = 'xml'
    pollingFrequencySeconds = 30
    urls = ['http://lol.com/services?artist=$','http://lol.com/services/song=$']
    artist = BinderKey(id='artist', type='xs:string', paramType='path')
    song = BinderKey(id='song', type='xs:string', paramType='path', required='true')
    

class TestTable(TableModel):
    name = 'Test'
    author = 'Josue Kouka'
    apiKeyURL = 'http://josuebrunel.org/api'
    documentationURL = 'http://josuebrunel.org/doc.html'
    sampleQuery = 'SELECT * FROM mytable'
    select = SelectBinder


```

* Generate your table in XML

```shell
$ myql-cli table --create lol
$ ls -l lol
Test.xml     __init__.py  __init__.pyc tables.py    tables.pyc
```

```shell
$ cat lol/Test.xml
```

```xml
<?xml version="1.0" ?>
<table https="false" securityLevel="any" xmlns="http://query.yahooapis.com/v1/schema/table.xsd">
    <meta>
        <author>Josue Kouka</author>
        <apiKeyURL>http://josuebrunel.org/api</apiKeyURL>
        <documentationURL>http://josuebrunel.org/doc.html</documentationURL>
        <description/>
        <sampleQuery>SELECT * FROM mytable</sampleQuery>
    </meta>
    <bindings>
        <select itemPath="products.product" pollingFrequencySeconds="30" produces="xml">
            <urls>
                <url>http://lol.com/services?artist=$</url>
                <url>http://lol.com/services/song=$</url>
            </urls>
            <inputs>
                <key id="song" paramType="path" required="true" type="xs:string"/>
                <key id="artist" paramType="path" required="false" type="xs:string"/>
            </inputs>
        </select>
    </bindings>
</table>
```

Voila

