# Python with SQL
## Contents 
* **Using PYODBC**
* **What is Cursor?**

# Introduction
* We can use a database with Python to meet customer needs. 
* Connection is achieved via API calls.   
![diagram](sql%20diagram.png)
## Using PYODBC
* PYODBC - Python Open Database Connectivity
* We use this to connect to SQL from our Python program
## What is cursor
* **some functions that we can use to interact with SQL data**

# Steps

### Installation
* Install the pyodbc package:
```
pip install pyodbc
```

* **Install Drivers** Use the following commands to install drivers required for compatibility with MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools
```

```
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
```
    
```
 brew install msodbcsql17 mssql-tools
```
* Once installed, create a python_sql.py file. 

### Setting up a connection
1. Import the pyodbc module 
2. Test the pyodbc module has been imported 
2. Define the server properties i.e. server, database, username and password. Store these as variables.
```python
import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "*****"
password = "******"
```
3. Establish a connection with the following command.
```python
# server name - database name - username and password is required to connect to pyodbc
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```

4. Use the cursor function to execute queries. Cursor is location of your mouse/current path
```python
cursor = northwind_connection.cursor()
```


### Running Queries
* We have now established a connection, we can access the database.
* We know that we have a table called Customers that has customer data available.
* Using ```fetchall()``` method, we can get all the data available in the customers table.
```python
cust_row=cursor.execute("SELECT * FROM Customers").fetchall()
for records in cust_row:
    print(records)
```
* We have another table in the DB called Products
```python
product_rows = cursor.execute("SELECT * FROM Products").fetchall()

```
* As with SQL, we can fetch a particular column using control flow. 
```python
# For each row in the database, print the UnitPrice
for x in product_rows:
    print(x.UnitPrice)
```

*  We can use a  while loops to ensure we only iterate through the data as long as the data is available.
* ```while True``` is used to create an infinite loop which will only stop when the break condition is met.

```python
product_row=cursor.execute("SELECT * FROM Products")
while True:
    # Returns one row at a time
    records= product_row.fetchone()
    # When no records left (value is None), stops
    if records is None:
        break
    print(records.UnitPrice)
```




