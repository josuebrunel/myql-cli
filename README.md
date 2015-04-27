### MYQL-CLI

[![Build Status](https://travis-ci.org/josuebrunel/myql-cli.svg)](https://travis-ci.org/josuebrunel/myql-cli) ![](https://readthedocs.org/projects/myql-cli/?badge=latest)

***MYQL-cli*** is a command line tool to run YQL queries or to generate YQL OpenTable

#### Installation

```shell
$ pip install myql # Not available yet
```
Alternative

In your virtualenv 

```shell
$ pip install git+https://github.com/josuebrunel/myql.git
$ git clone https://github.com/josuebrunel/myql-cli.git
$ cd myql-cli
$ python setup.py install --record files.txt
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

* ___json___ 

```shell
$ myql-cli execute --format json "select * from geo.countries where name='Congo'"
```
```json
{
    "query": {
        "count": 1,
        "lang": "en-US",
        "results": {
            "place": {
                "lang": "en-US",
                "woeid": "23424779",
                "uri": "http://where.yahooapis.com/v1/place/23424779",
                "name": "Congo",
                "placeTypeName": {
                    "content": "Country",
                    "code": "12"
                }
            }
        },
        "created": "2015-04-07T12:37:13Z"
    }
}
```

* ___xml___

```shell
$ myql-cli execute --format xml "select * from geo.countries where name='Congo'"
```
```xml
<?xml version="1.0" ?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2015-04-07T12:36:44Z" yahoo:lang="en-US">
    <results>
        <place xml:lang="en-US" xmlns="http://where.yahooapis.com/v1/schema.rng" yahoo:uri="http://where.yahooapis.com/v1/place/23424779">
            <woeid>23424779</woeid>
            <placeTypeName code="12">Country</placeTypeName>
            <name>Congo</name>
        </place>
    </results>
</query>
<!-- total: 113 -->
<!-- pprd1-node1021-lh2.manhattan.bf1.yahoo.com -->
```

* ___xml + diagnostics___

```shell
$ myql-cli execute --format xml --diagnostics "select * from geo.countries where name='Congo'"
```
```xml
<?xml version="1.0" ?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2015-04-07T12:38:43Z" yahoo:lang="en-US">
    <diagnostics>
        <publiclyCallable>true</publiclyCallable>
        <url execution-start-time="2" execution-stop-time="71" execution-time="69">
<![CDATA[http://wws.geotech.yahooapis.com/v1/countries;start=0;count=1000]]>        </url>
        <user-time>74</user-time>
        <service-time>69</service-time>
        <build-version>0.2.75</build-version>
    </diagnostics>
    <results>
        <place xml:lang="en-US" xmlns="http://where.yahooapis.com/v1/schema.rng" yahoo:uri="http://where.yahooapis.com/v1/place/23424779">
            <woeid>23424779</woeid>
            <placeTypeName code="12">Country</placeTypeName>
            <name>Congo</name>
        </place>
    </results>
</query>
<!-- total: 74 -->
<!-- pprd1-node1016-lh3.manhattan.bf1.yahoo.com -->
```

* ___json + diagnostics + debug___

```shell
$ myql-cli execute --format json --diagnostices --debug "select * from geo.countries where name='Congo'"
```
```json
{
    "query": {
        "count": 1,
        "lang": "en-US",
        "diagnostics": {
            "url": [
                {
                    "content": "http://sherpa-bcp5903.dht.yahoo.com:4080/YDHTWebService/V1/get/yql.global/store%3A%2F%2Fdatatables.org%2Falltableswithkeys",
                    "execution-stop-time": "5",
                    "execution-start-time": "1",
                    "execution-time": "4",
                    "id": "3a511b18-0e52-405d-b804-803933d620eb"
                },
                {
                    "content": "http://sherpa-bcp5903.dht.yahoo.com:4080/YDHTWebService/V1/get/yql.global/store%3A%2F%2FRjdEzitN2Hceujh3tGHPj6",
                    "execution-stop-time": "17",
                    "execution-start-time": "7",
                    "execution-time": "10",
                    "id": "ddd7fc5d-b63d-4988-9437-fb678f781e46"
                },
                {
                    "content": "http://sherpa-bcp5903.dht.yahoo.com:4080/YDHTWebService/V1/get/yql.global/store%3A%2F%2FRjdEzitN2Hceujh3tGHPj6",
                    "execution-stop-time": "53",
                    "execution-start-time": "42",
                    "execution-time": "11",
                    "id": "43b945b6-b92a-4e74-a58c-9a7b597a8045"
                },
                {
                    "content": "http://wws.geotech.yahooapis.com/v1/countries;start=0;count=1000",
                    "execution-stop-time": "156",
                    "execution-start-time": "79",
                    "execution-time": "77"
                }
            ],
            "user-time": "160",
            "build-version": "0.2.75",
            "service-time": "102",
            "publiclyCallable": "true"
        },
        "results": {
            "place": {
                "lang": "en-US",
                "woeid": "23424779",
                "uri": "http://where.yahooapis.com/v1/place/23424779",
                "name": "Congo",
                "placeTypeName": {
                    "content": "Country",
                    "code": "12"
                }
            }
        },
        "created": "2015-04-07T12:39:47Z"
    }
}
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
  -i, --init    Creates a project with a tables.py file in it
  -c, --create  Creates tables in the tables.py file of your project
```

* Initialize the table project

```shell
$ myql-cli table -i lol
$ ls -l lol
__init__.py tables.py
```

* Define your table

```shell
$ vim lol/tables.py
```

```python
from myql.contrib.table import BinderModel, BinderKey, BinderPage, TableModel, BinderFrom

class SelectBinder(BinderModel):
    name = 'select'
    itemPath = 'products.product'
    produces = 'xml'
    pollingFrequencySeconds = 30
    urls = ['http://lol.com/services?artist={artist}','http://lol.com/services/song={song}']
    paging = BinderPage('page', {'id': 'ItemPage', 'default': '1'}, {'id':'Count' ,'max':'25'},{'default': '10'})
    artist = BinderKey(id='artist', type='xs:string', paramType='path')
    song = BinderKey(id='song', type='xs:string', paramType='path', required='true')
    

class TestTable(TableModel):
    name = 'Test'
    author = 'Josue Kouka'
    apiKeyURL = 'http://josuebrunel.org/api'
    documentationURL = 'http://josuebrunel.org/doc.html'
    sampleQuery = ['SELECT * FROM mytable']
    select = BinderFrom(SelectBinder)


```

* Generate your table in XML

```shell
$ myql-cli table --create lol
$ ls lol
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
                <url>http://lol.com/services?artist={artist}</url>
                <url>http://lol.com/services/song={song}</url>
            </urls>
            <inputs>
                <key id="song" paramType="path" required="true" type="xs:string"/>
                <key id="artist" paramType="path" required="false" type="xs:string"/>
            </inputs>
            <paging model="page">
                <start default="1" id="ItemPage"/>
                <total default="10"/>
                <pageSize id="Count" max="25"/>
            </paging>
        </select>
    </bindings>
</table>
```

Voila

