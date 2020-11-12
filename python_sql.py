import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
# Create a connection using pyodbc.connect(server name, database name, username, password)
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# We have now established a connection, we can access the database.
# Cursor is a built in function in pyodbc which provides the location of your mouse/current path
cursor = northwind_connection.cursor()
# Cursor is used in conjunction with the execute command to run queries.

# EXAMPLE 1 : Basic Queries
# Select the version of your current DB
cursor.execute("SELECT @@VERSION")
row = cursor.fetchone()
print(row)

# EXAMPLE 2 - For loops
# We know that we have a table called Customers that has customer data available.
# Using fetchall method, we can get all the data available in the customers table.
cust_row=cursor.execute("SELECT * FROM Customers").fetchall()
# Use a for loop to iterate through the rows and print as a list.
for records in cust_row:
    print(records)

# EXAMPLE 3 - Specific Columns
# We have another table in the DB called Products
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# As with SQL, we can fetch a particular column.
# For each row in the database, print the UnitPrice
for x in product_rows:
    print(x.UnitPrice)


# EXAMPLE 4 - While loops
# Combination of our loop and control flow to ensure we only iterate through the data as long as the data is available.
product_row=cursor.execute("SELECT * FROM Products")
# While True is used to create an infinite loop which will only stop when the break condition is met.
while True:
    records= product_row.fetchone()
    # When no records left (value is None), stops
    if records is None:
        break
    print(records.UnitPrice)