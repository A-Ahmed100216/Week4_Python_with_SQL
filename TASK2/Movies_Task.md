# Python with SQL Exercise 2 -  SQL Movies


## Iteration 1
#### Summary
Now that you've learned how to connect to the DB using pyodbc you can start abstracting out interaction the db! This is great if you don't like writing sql.

#### Tasks
* CRUD the DB (Hint: create abstraction and methods to deal with db so you don't have to)


#### Acceptance Criteria
* You can get all the movies
* You can search based on title
* You can add movies to DB


## Second iteration: IMDB CSV <> Py <> SQL

### Summary
You know how to parse txt files into python, connect python into the db, and 
manipulate and change data with python.  
Your task is to move data from text files into the db and from the the db into text files

### Tasks
* Read the text file and create object
* Save object in DB
* Load that from DB and create object
* Output object to text file
#### Extra:
* Explore other APIs

### Acceptance Criteria
* Able to take in 10 film names in text file and save to db
* Able to load data from DB and create text file with names


# Process
1. Download the csv file containing the movie data and store in this project directory.
2. Import relevant classes and packages:   
The Connection class as this will be a parent class used to connect to the database.   
The ```pandas``` package which will be used to read the csv file.
```python
from TASK1.OOP_SQL import Connection
import pandas
```
3. Create a Movies class which will be a child of Connection. Initialise the class so it inherits parent attributes i.e. the ability to connect to the database. Then utilise the pandas package to read the csv file and create a dataframe with the columns from the csv file. 
```python
class Movies(Connection):
    # Initialise class and inherit parent attributes
    def __init__(self):
        super().__init__()
        # Import the table
        self.data = pandas.read_csv(r'imdbtitles.csv')
        self.df = pandas.DataFrame(self.data,
                              columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                                       'runtimeMinutes', 'genres'])
```
4. Define a method for creating a table in the Northwind database. This requires running a a query to create a table.  
```python
 # Method for creating a table
    def create_table(self):
        movies=self.cursor.execute("CREATE TABLE movie_info (movie_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,titleType VARCHAR(50), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult VARCHAR(10), startYear VARCHAR(10), endYear VARCHAR(10), runtimeMinutes VARCHAR(10) , genres VARCHAR(255))")
```
5. Once the table is created within the database, data can be added to it. The following method iterates through the csv file and creates a variable for each of the columns. This is then inserted via executing the relevant sql command. Finally the changes must be committed to the database. 
```python
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
```

6. The show movies function simply executes a query to fetch all the rows and then use a for loop to return as single lines.
```python
    def show_movies(self):
        movie_info=self.cursor.execute("SELECT * FROM movie_info").fetchall()
        for x in movie_info:
            print(x)
```

7. As per the requirements, the user is able to search a movie/series by name therefore this is achieved by taking a user input and formatting it into a conditional query where the condition is to select all rows which match the user input. 
```python
    def search_by_name(self):
        # Ask user the input the name of the movie they are looking for
        name=input("Please type the name of the movie you are looking for: ")
        # Run a query to select all rows which match the name of the movie they are looking for
        search_name=self.cursor.execute(f"SELECT * from movie_info WHERE primaryTitle='{name}'").fetchone()
        print(search_name)
```
8. Another requirement is for users to add their own data. This requires users to inpu their own data and format this into a SQL command.
```python
    def add_new_data(self):
        titletype = input("Please enter the type of data you wish to input i.e. movie, short, series: ")
        primary = input("Please enter the tile of the movie/series: ")
        original = input("Please enter the original name of the movie/series: ")
        adult = input("Is the movie adult rated. Yes=1, No=0")
        start = input("Please enter the year of release: ")
        end = input("Please enter the year of ending: ")
        runtime = input("Please enter the runtime in minutes: ")
        genre = input("Please enter the genre(s) i.e. horror, action etc.: ")
        if "'" in primary or original:
            primary = primary.replace("'", "''")
            original = original.replace("'", "''")
        self.cursor.execute(
            f"INSERT INTO movie_info (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES ('{titletype}', '{primary}', '{original}','{adult}','{start}','{end}','{runtime}','{genre}')")

```
9. Instantiate the class and execute methods. The create_table mehtod cn only be executed once otherwise it will throw an error as the object already exists. 
```python
test=Movies()
# test.create_table()
test.add_data()
test.show_movies()
test.search_by_name()
test.add_new_data()
```
