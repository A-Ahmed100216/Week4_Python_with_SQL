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