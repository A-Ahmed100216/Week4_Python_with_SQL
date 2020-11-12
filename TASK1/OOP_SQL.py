# 1. Create a new file and class with function to establish connection with pyodbc.
# 2. Create a function that creates a table in DB
# 3. Create a function that prompts user to input data into the table.
# 4. Create a new file called PYODBC_TASK.md and document the steps to implement the task
import pyodbc

# Create a connection class
class Connection:
    # class initialisation
    def __init__(self):
        # Define DB parameters
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        # Establish connection
        self.northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        # Set up cursor
        self.cursor = self.northwind_connection.cursor()

# class Tables(Connection):
    # Define a function to create a new table
    def new_table(self):
        # Create a table with an columns for id, name, type, and age
        self.cursor.execute("CREATE TABLE Mina_Petstore (id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), age INT)")
        # Access the rows in this table and store the newly created table in a variable.
        Mina_Petstore = self.cursor.execute("SELECT * FROM Mina_Petstore").fetchall()
        return (Mina_Petstore)




    # Define a function to take user input
    def user_input(self):
        # Ask the user to input each of the columns
        # while True:
        name_input = input("Enter pet name: ")
        type_input = input("Type of pet: ")
        age_input = int(input("Enter pet age: "))
        # Insert values into the table
        self.cursor.execute(f"INSERT INTO Mina_Petstore (name, type, age) VALUES('{name_input}', '{type_input}', {age_input})")
            # if name_input=="":
            #     break

        Mina_Petstore = self.cursor.execute("SELECT * FROM Mina_Petstore").fetchall()
        return Mina_Petstore


# testing=Tables()
# print(testing.new_table())
# print(testing.user_input())
