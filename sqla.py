# create a SQLite3 database and table

## import the sqlite3 library
import sqlite3

## create a new database if the dabase doesn't already exist
conn = sqlite3.connect("new.db")

## get a cursor object used to execute SQL commands
cursor = conn.cursor()

## create a table
cursor.executescript(
	'''DROP TABLE IF EXISTS population;
	CREATE TABLE population(city TEXT, state TEXT, population INT);
	''')

## close the database connection
conn.close()
