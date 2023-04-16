# Corbyn Eaker
# Modules_and_Databases pt2.py
# This program solves problems 16.3-16.8

# Importing csv and sqlite3 modules
import csv
import sqlite3 as sq
import sqlalchemy as sa
from sqlalchemy import text

# 16.3
# Saving text to be stored in CSV file in variable
text1 = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

# Opening book2.csv and writing the variable text1 to is, then closing the file
file1 = open('book2.csv', 'w')
file1.write(text1)
file1.close()

# 16.4 and 16.5
# Opening book2.csv in read mode
with open('book2.csv', 'r') as file:
    # Creating csv reader object ()
    reader = csv.reader(file)
    # skipping the header row (this took me hours to find out how to do, but it was so simple)
    next(reader)
    # setting up connection to the database
    conn = sq.connect('books.db')
    curs = conn.cursor()
    # creating the table if it doesn't already exist
    curs.execute('''CREATE TABLE IF NOT EXISTS books 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                author TEXT, 
                year INTEGER)''')
    # iterating through the table to insert data
    for row in reader:
        curs.execute('''INSERT INTO books (title, author, year) VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

# 16.6
    # Selecting the titles of book and ordering them by title, ascending
    curs.execute('SELECT title FROM books ORDER BY title')
    # assigning rows retrieved to be iterated through
    rows = curs.fetchall()
    # iterating through rows and printing each item
    for row in rows:
        print(row)

# 16.7
    # Selecting the all books and sorting them by year of publication, ascending
    curs.execute('SELECT * FROM books ORDER BY year')
    # assigning rows retrieved to be iterated through
    rows = curs.fetchall()
    # iterating through rows and printing each item
    for row in rows:
        print(row)

# closing connection to the database
conn.close()


# 16.8 [NOT COMPLETE] final print statement will not print anything
# creating variable for engine and connection object
engine = sa.create_engine('sqlite:///books.db', echo=None)
conn2 = engine.connect()
# using the connection object to execute the query, had to import text and call it on the variable with the query stored inside
query = 'SELECT * FROM books ORDER BY year'
result = conn2.execute(text(query))
# fetching all data returned from query and storing it in rows2 variable
rows2 = result.fetchall()
# this should print the stored query results, having a very hard time getting this to print
for row in rows2:
    print(row)
# closing connection to database
conn2.close()

