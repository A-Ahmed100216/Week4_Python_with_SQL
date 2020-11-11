import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "**"
password = "**"
# Creae a connection
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# server name - database name - username and password is required to connect to pyodbc

# Use cursor which is a built in function in pyodbc
# Cursor is location of your mouse/current path
cursor = northwind_connection.cursor()
# cursor.execute("SELECT @@VERSION")
# Select the version of your current DB
# row = cursor.fetchone()
# print(row)

# We have now established a connection, we can access the database.
# We know that we have a table called Customers that has customer data available.

# Using fetchall method, we can get all the data available in the customers table.
cust_row=cursor.execute("SELECT * FROM Customers").fetchall()
for records in cust_row:
    print(records)

# We have another table in the DB called Products
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# As with SQL, we can fetch a particular column.
# For each row in the database, print the UnitPrice
for x in product_rows:
    print(x.UnitPrice)


product_row=cursor.execute("SELECT * FROM Products")
# Getting the Product table and data
# Iterate through the data until the last line of the data (until the condition is false:

# Combination of our loop and control flow to ensure we only iterate through the data as long as the data is available.
while True:
    records= product_row.fetchone()
    # When no records left (value is None), stops
    if records is None:
        break
    print(records.UnitPrice)


