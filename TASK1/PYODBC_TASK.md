#Python with SQL Exercise

## Increment 1 Tasks
* Create a new file and class with function to establish connection with pyodbc.
* Create a function that creates a table in DB
* Create a function that prompts user to input data into the table.
* Create a new file called PYODBC_TASK.md and document the steps to implement the task
### Process 
1. Import the pyodbc module and initialise if this has not been done so. See [documentation](../README.md)for more information.
```python
import pyodbc
```

2. Create a Connection class
```python
class Connection:
```

3. Initialise the class with attributes of the database. These are the server, database name, username, and password. Establish the connection using these parameters and store as a separate attribute. Finally, set up an attribute for cursor.  
```python
# Create a connection class
    # class initialisation
    def __init__(self):
        # Define DB parameters
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "**"
        self.password = "*********"
        # Establish connection
        self.northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        # Set up cursor
        self.cursor = self.northwind_connection.cursor()
```
4. Define a function to create a new table.
```python
    # Define a function to create a new table
    def new_table(self):
        # Create a table with an columns for id, name, type, and age
        self.cursor.execute("CREATE TABLE Mina_Petstore (id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), age INT)")
        # Access the rows in this table and store the newly created table in a variable.
        Mina_Petstore = self.cursor.execute("SELECT * FROM Mina_Petstore").fetchall()
        return (Mina_Petstore)
```
5. Define a function to take user inputs and add to the table. 
```python
    # Define a function to take user input
    def user_input(self):
        # Ask the user to input each of the columns
        name_input = input("Enter pet name: ")
        type_input = input("Type of pet: ")
        age_input = int(input("Enter pet age: "))
        # Insert values into the table
        self.cursor.execute(f"INSERT INTO Mina_Petstore (name, type, age) VALUES('{name_input}', '{type_input}', {age_input})")
        Mina_Petstore = self.cursor.execute("SELECT * FROM Mina_Petstore").fetchall()

        return Mina_Petstore
```
6. Instantiate the class
```
testing=Connection()
print(testing.new_table())
print(testing.user_input())
```


## Increment 2 Tasks
#### Summary
An sql manager for the products table
create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.

As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.
#### Tasks
* Create two files nw_products.py & nw_runner.py and then we will move into creating our object.
* We've had a requirement for the stock department to print out the average value of all of our stock items.

**!!!Important Note!!!** It would be more efficient to write the SQL query to find the data and compute the value and simply return the value in Python.

### Process
1. Import the Parent class connection
```python
from TASK1.OOP_SQL import Connection
```
2. Create a class for the stock department which will be a child of Connection. Initialise the class and user the ```super()``` method to inherit parent attributes. This inheritance will enable the class to connect to the database. Within this initialisation method, define a query to obtain all the rows within the Products table. 
```python
class StockDepartment(Connection):
    def __init__(self):
        super().__init__()
        self.products=self.cursor.execute("SELECT * FROM Products").fetchall()
```
3. As this class pertains to stock, create a method to print the stock of each product and return as a formatted string.
```python
def stock(self):
        for item in self.products:
            print("{} has {} units in stock".format(item.ProductName,item.UnitsInStock))
```
4. The crux of this task is to print out the average value of all the stock items. This can be achieved by executing the query to calcualte this value and simply printing in a fomratted string. The query is as follows:
```
SELECT AVG(UnitsInStock) FROM Products WHERE UnitsInStock!=0
```
 This query will obtain the average of the column UnitsInStock, provided the value is not 0. This condition has been introduced to prevent out-of-stock items skewing the average result. The query can then be executed in python and printed as a formatted string. As the output of the query execution is a nested list, the formatted string accesses the index at which the average value is given. 
```python
    # Define a method to calculate the average of items in stock.
    def average_stock(self):
        # Use a query to calculate the average stock where stock is not 0 as this would skew results.
        avg_stock= self.cursor.execute("SELECT AVG(UnitsInStock) FROM Products WHERE UnitsInStock!=0").fetchall()
        # The query can be formatted into a string
        print("\nThe average number of items in stock is {}".format(avg_stock[0][0]))
```
