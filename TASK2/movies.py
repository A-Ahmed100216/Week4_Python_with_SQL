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

    # Add the csv data to the table in the northwind database
    def add_data(self):
        # iterate through the csv file and determine which column each value belongs to.
        for row in self.df.itertuples():
                titletype=row.titleType
                primary = row.primaryTitle
                original=row.originalTitle
                adult = row.isAdult
                start = row.startYear
                end = row.endYear
                runtime = row.runtimeMinutes
                genre = row.genres
                # If the name contains an apostrophe, the for loop replaces with '' as this is an escape character.
                if "'" in primary or original:
                    primary = primary.replace("'","''")
                    original = original.replace("'","''")
                # Execute the insert command, replacing the values with the variables deifned just above
                self.cursor.execute(f"INSERT INTO movie_info (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES ('{titletype}', '{primary}', '{original}','{adult}','{start}','{end}','{runtime}','{genre}')")
        # Commit to the database
        self.northwind_connection.commit()

    # Define a function to show movies
    def show_movies(self):
        movie_info=self.cursor.execute("SELECT * FROM movie_info").fetchall()
        # Print as rows.
        for x in movie_info:
            print(x)

    # Define a method for users to search for a movie by name
    def search_by_name(self):
        # Ask user the innput the name of the movie they are looking for
        name=input("Please type the name of the movie you are looking for: ")
        # Run a query to select all rows which match the name of the movie they are looking for
        search_name=self.cursor.execute(f"SELECT * from movie_info WHERE primaryTitle='{name}'").fetchone()
        print(search_name)

    # Define a method for users to add their own data
    def add_new_data(self):
        # Ask users to input data for all the columns.
        titletype = input("Please enter the type of data you wish to input i.e. movie, short, series: ")
        primary = input("Please enter the title of the movie/series: ")
        original = input("Please enter the original name of the movie/series: ")
        adult = input("Is the movie adult rated. Yes=1, No=0 ")
        start = input("Please enter the year of release: ")
        end = input("Please enter the year of ending: ")
        runtime = input("Please enter the runtime in minutes: ")
        genre = input("Please enter the genre(s) i.e. horror, action etc.: ")
        # If the name contains an apostrophe, replace with escape characters.
        if "'" in primary or original:
            primary = primary.replace("'", "''")
            original = original.replace("'", "''")
        # Execute query
        self.cursor.execute(
            f"INSERT INTO movie_info (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES ('{titletype}', '{primary}', '{original}','{adult}','{start}','{end}','{runtime}','{genre}')")

    # Define method to create a new csv
    def new_csv(self):
        # Ask the user to input their query
        query=input("Please enter your query")
        # Update the database with the query
        updated =pandas.read_sql_query(f'{query}', self.northwind_connection)
        # Create a dataframe of the updated table
        new_df=pandas.DataFrame(updated)
        # Convert to csv
        new_df.to_csv(r'\PycharmProjects\Week4_Python_with_SQL\TASK2\new_movie.csv')
        # Print the new dataframe
        print(new_df)


# Instantiate class
test=Movies()
# test.create_table()
# test.add_data()
# test.search_by_name()
# test.add_new_data()
# test.show_movies()
# test.new_csv()