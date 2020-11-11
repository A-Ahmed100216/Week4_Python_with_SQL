# Create a connection class
class Connection:
    # class initialisation
    def __init__(self):
        # Define DB parameters
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "**"
        self.password = "*****"
        # Establish connection
        self.northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        # Set up cursor
        self.cursor = self.northwind_connection.cursor()

    def new_table(self):
        self.cursor.execute("CREATE TABLE Aminah_Petstore (id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), age INT)")
        Aminah_Petstore = self.cursor.execute("SELECT * FROM Aminah_Petstore").fetchall()
        return (Aminah_Petstore)

    def view_table(self):
        for x in Aminah_Petstore:
            return x


testing=Connection()
print(testing.new_table())
# print(testing.view_table())