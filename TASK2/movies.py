from TASK1.OOP_SQL import Connection
# Import the pandas package enabling us to read the csv file
import pandas

# Create a Movies class with a parent as Connection to connect to the database.
class Movies(Connection):
    # Initialise class and inherit parent attributes
    def __init__(self):
        super().__init__()

    # Method for creating a table
    def create_table(self):
        data = pandas.read_csv(r'imdbtitles.csv')
        df = pandas.DataFrame(data,
                              columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                                       'runtimeMinutes', 'genres'])
        movies=self.cursor.execute("CREATE TABLE movie_info (movie_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,titleType VARCHAR(50), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult VARCHAR(10), startYear VARCHAR(10), endYear VARCHAR(10), runtimeMinutes VARCHAR(10) , genres VARCHAR(255))")
        for row in df.itertuples():
                titletype=row.titleType
                primary = row.primaryTitle
                original=row.originalTitle
                adult=row.isAdult
                start=row.startYear
                end=row.endYear
                runtime=row.runtimeMinutes
                genre=row.genres
                self.cursor.execute(f"INSERT INTO Northwind.dbo.movie_info (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES ('{titletype}', '{primary}', '{original}','{adult}','{start}','{end}','{runtime}','{genre}')")
        self.northwind_connection.commit()
        movie_info=self.cursor.execute("SELECT * FROM movie_info").fetchall()
        for x in movie_info:
            print(x)
        # print(movie_info)



    #
    # def search_by_name(self):
    #     name=input("Please type the name of the movie you are looking for: ")


test=Movies()
test.create_table()