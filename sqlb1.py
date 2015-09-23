# inserting data - using more compact code

## import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute('''INSERT INTO population VALUES('New Yourk City', 'NY', 8200000)''')
    c.execute('''INSERT INTO population VALUES('San Francisco', 'CA', 800000)''')
# no need to commit changes to database when using "with sqlite.connect"
