# Using Pandas to compare files

## Table of contents
- [Overview](#overview)
- [Prerequisites](#prereq)
- [Example Code](#examplecode)
- [References](#references)

<div id='overview'/>

## Overview

When comparing large files, the normal assumption is using relational SQL databases. The popular programs we think ofm ones that reach outside comptuer science knowledge, are MySQL, PostgreSQL, MSSQL, etc. Although such databases harbor multiple advantages, problems derive from the structured query language, resulting in complex and disconcerting data. 

Another disadvantage regarding the relational databases is the layer of security. In typical scenarios, databases are guarded behind layers of administration. This causes the double problem of not only acquiring the data becoming a hurdle more than a task, but leaves frustration behind the user. 

Running large queries on a SQL database also enhances performance problems for production environments, furhtring accumulating frustration. Taken from experience the security layers and perfromance hinderances, numerous database administrators DBA(s) refuse open-read access to the database. In response, we now have Pandas which allows users to construct queries focusing on analytical and natural language perspective wihtout negative resistance on IT infrastructure.



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
 - [Indexing and Selecting Data with Pandas](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)
