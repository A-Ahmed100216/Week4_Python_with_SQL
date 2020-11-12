from TASK1.OOP_SQL import Connection
import pandas

class Movies(Connection):
    def __init__(self):
        super().__init__()

    def create_table(self):
        data = pandas.read_csv(r'imdbtitles.csv')
        df = pandas.DataFrame(data,
                              columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                                       'runtimeMinutes', 'genres'])
        movies=self.cursor.execute('CREATE TABLE movie_info (movie_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,titleType VARCHAR(50), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult VARCHAR(10), startYear DATE, endYear DATE, runtimeMinutes INT , genres VARCHAR(255)')
        for row in df.itertuples():
                titletype=row.titleType
                primary = row.primaryTitle
                original=row.originalTitle
                adult=

                self.cursor.execute(f"INSERT INTO movie_info (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES ('{titletype}', '{primary}', '{original}','{adult}','{start}','{end}','{runtime}','{genre}')")





    def search_by_name(self):
        name=input("Please type the name of the movie you are looking for: ")
        rsult = self.cursor.execute("SELECT * FROM {}".format(movies))

