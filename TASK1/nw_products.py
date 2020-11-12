from TASK1.OOP_SQL import Connection

#  Create a class for the stock department
class StockDepartment(Connection):
    def __init__(self):
        super().__init__()
        self.products=self.cursor.execute("SELECT ProductName FROM Products").fetchall()

    # We've had a requirement for the stock department to print out the average value of all of our stock items.
    def stock(self):
        stock=self.products
        return stock

        # stock=self.cursor.execute("SELECT * ")
        # print(self.products)





