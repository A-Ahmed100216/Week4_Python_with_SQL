from TASK1.OOP_SQL import Connection

#  Create a class for the stock department
class StockDepartment(Connection):
    def __init__(self):
        super().__init__()
        self.products=self.cursor.execute("SELECT * FROM Products").fetchall()

    # We've had a requirement for the stock department to print out the average value of all of our stock items.
    def stock(self):
        for item in self.products:
            print("{} has {} units in stock".format(item.ProductName,item.UnitsInStock))

    def average_stock(self):
        # Use a query to calculate the average stock where stock is not 0 as this would skew results.
        avg_stock= self.cursor.execute("SELECT AVG(UnitsInStock) FROM Products WHERE UnitsInStock!=0").fetchall()
        # The query can be formatted into a string
        print("\nThe average number of items in stock is {}".format(avg_stock[0][0]))


tester=StockDepartment()
tester.stock()
tester.average_stock()






