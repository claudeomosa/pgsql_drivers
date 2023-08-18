Psycopg 3
===================================================

[Psycopg](https://github.com/psycopg/psycopg) 3 is a modern implementation of a PostgreSQL adapter for Python. For installation, you can visit their [github](https://github.com/psycopg/psycopg) and their documentation can be found in their official [website](https://www.psycopg.org/psycopg3/). 
This version has methods that return records in JSON format. 


Usage
------------
change to this directory to work on the package's source code:

```shell
cd psycopg
```

In order to work on the Psycopg source code you need to have the ``libpq``
PostgreSQL client library installed in the system. For instance, on Debian
systems, you can obtain it by running::

```shell
sudo apt install libpq5
```


Please note that the repository contains the source code of several Python
packages: that's why you don't see a ``setup.py`` here. The packages may have
different requirements, in this version we will only be working with the ``psycopg`` directory which contains the pure python implementation. If you wish to work on ``psycopg_c`` directory containing an optimization module written in C/Cython or ``psycopg_pool`` directory containing the `connection pools` implementations, check [Psycopg](https://github.com/psycopg/psycopg) for instructions.


You can create a local virtualenv and install there the packages::

    python -m venv .venv
    source .venv/bin/activate
    pip install -e "./psycopg[dev,test]"    # for the base Python package


Now change to the ``psycopg`` directory:

```shell
cd psycopg
```

You can then make changes to the `main.py` file with your db credentials and a few queries to test.
1. `cur.fetchall_as_json()` returns all records in the following format:

```python
{
    "data": [
        {
            "project_id": 3,
            "user_id": 2
        },
        {
            "project_id": 3,
            "user_id": 1
        },
        {
            "project_id": 6,
            "user_id": 3
        },
        {
            "project_id": 4,
            "user_id": 1
        },
    ],
    "status_code": 200
}
```

2. `cur.fetchone_as_json()` returns a single record as follows:

```python
{
    "data": [
        {
            "project_id": 3,
            "user_id": 2
        }
    ],
    "status_code": 200
}
```

3. `cur.fetchmany_as_json(size=2)` returns 2 records as follows:

```python
{
    "data": [
        {
            "project_id": 3,
            "user_id": 2
        },
        {
            "project_id": 3,
            "user_id": 1
        }
    ],
    "status_code": 200
}
```


You can run the following to build and create a wheel distribution of this package:

```shell
python setup.py bdist_wheel 
```
