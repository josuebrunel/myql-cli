### LokingYQL-CLI

***LokingYQL-cli*** is a command line tool to make YQL queries through the command line

#### Installation

```shell
$ pip install lokingyql # Not available yet
```

Or by downloading the package and performing

```shell
$ python setup.py install --record files.txt # the record just to help when uninstalling the tool
```

#### How To

##### Query Tool

```shell
$ lokingyql-cli execute -h
```

```shell
$ lokingyql-cli execute --format json "select name from geo.states where place='Congo'"
```

##### YQL Shell

```shell
$ lokingyql-cli shell -h
```

```shell
$ lokingyql-cli shell
yql> 
```

##### Table Manager

```shell
$ lokingyql-cli table -h
```
