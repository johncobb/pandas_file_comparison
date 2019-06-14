# Using Pandas to compare files

## Table of contents
- [Overview](#overview)
- [Prerequisites](#prereq)
- [Example Code](#examplecode)
- [References](#references)

<div id='overview'/>

## Overview

When comparing large files we typically look to relational SQL databases like MySQL, PostgreSQL, MSSQL, etc. These are great tools but the query language can become complex and difficult to read. What's more is these databases are typically guarded behind layers of database administration which can make gaining access challenging. Running large queries on a SQL database can cause performance problems in production environments. For these reasons, many DBA(s) will not allow open read access to the database. Today we have Pandas which allows users to design queries in a more analytical and natural language perspective wihtout having a negative impact on IT infrastructure.



<div id='prereq'/>

## Prerequisites:

 - Installing PiP

```console
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

python get-pip.py --user
```

 - Installing Virtual Environment 
```console
pip install --user virtualenv
```

 - Initialize python3 in new virtual environment
```console
virtualenv -p python3 env
```

 - Activate environment  
```console
. env/bin/activate
```

 - Installing dependencies
```console
pip install -r requirements.txt
```

<div id='examplecode'/>

## Running the example code 

Run the code
```console
python3 run_pandas.py training/base_50 training/base_100
```
### What is the code doing?
Comparing:
 - Records in file1 not in file2 and the inverse
 - Subset of column in file1 not in subset of column in file2 and the inverse
 - Compare is file1 equal to file2


To stop the virtual session  
```console
deactivate
```


<div id='references'/>

## References
 - [Installing Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
 - [Python Data Analysis Library](https://pandas.pydata.org/)
 - [Storage of Pandas DataFrames](http://matthewrocklin.com/blog/work/2015/03/16/Fast-Serialization)