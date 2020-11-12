from TASK1.OOP_SQL import Connection
# Import the pandas package enabling us to read the csv file
import pandas

# Create a Movies class with a parent as Connection to connect to the database.
class Movies(Connection):
    # Initialise class and inherit parent attributes
    def __init__(self):
        super().__init__()
        # Import the table
        self.data = pandas.read_csv(r'imdbtitles.csv')
        self.df = pandas.DataFrame(self.data,
                              columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                                       'runtimeMinutes', 'genres'])

    # Method for creating a table
    def create_table(self):
        movies=self.cursor.execute("CREATE TABLE movie_info (movie_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,titleType VARCHAR(50), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult VARCHAR(10), startYear VARCHAR(10), endYear VARCHAR(10), runtimeMinutes VARCHAR(10) , genres VARCHAR(255))")

    def add_data(self):
        for row in self.df.itertuples():
                titletype=row.titleType
                primary = row.primaryTitle
                original=row.originalTitle
                adult = row.isAdult
                start = row.startYear
                end = row.endYear
                runtime = row.runtimeMinutes
                genre = row.genres
                if "'" in primary or original:
                    primary = primary.replace("'","''")
                    original = original.replace("'","''")
                self.cursor.execute(f"INSERT INTO movie_info (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES ('{titletype}', '{primary}', '{original}','{adult}','{start}','{end}','{runtime}','{genre}')")
        self.northwind_connection.commit()

    def show_movies(self):
        movie_info=self.cursor.execute("SELECT * FROM movie_info").fetchall()
        for x in movie_info:
            print(x)

    def search_by_name(self):
        name=input("Please type the name of the movie you are looking for: ")
        search_name=self.cursor.execute(f"SELECT {name} from movie_info").fetchone()



test=Movies()
# test.create_table()
test.add_data()