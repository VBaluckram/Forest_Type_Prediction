PGX Technical Interview Instructions:
1. Read all the instructions carefully
2. Import nesessary packages
3. Use Comments to describe classes, definitions, variables used etc..
4. Template Files data_to_sqlite3.py, model.py are provied to get a quick start
5. In addition to the template provided you can make use of new classes, definitions and properties 
6. Finally, complete the tasks given below

Tasks to be completed:
1. Load Data into SQLite3 using the provided `data_to_sqlite3.py` script.
    a. The only modification that is needed is the path to the data file
    b. This is meant to make sure you have your environment properly set up to
    work with the data in SQL and are able to utilize others code.
    c. It also provides some example code that you can use in the next part

2. Read Data from SQLite3
	a. Read data from Sqlite3 database into pandas dataframe using sqlalchemy and pandas
	b. Use the template available in /pgx_interview/model.py -> load_data()

3. Build Models
	a. Make use of the data read from the SQLite
    b. Provide a brief overview of data exploration conducted to assist in
    modeling
    c. Build a model to correctly predict the `Label` column in the data using
    any other available columns
	     i. Feel free to use any Python library (scikit learn, tensorflow,
         pytorch, etc.)
