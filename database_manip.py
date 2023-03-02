import sqlite3 # imports SQLLite3 module

#  Creates or opens a file called python_programming_db with a SQLite3 DB & assigns
db = sqlite3.connect('python_programming_db')

# creates a cursor object to exectue SQL statements
cursor = db.cursor()

# uses cursor object to create 'python_programming' table
cursor.execute('''
CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER);
''')

# saves changes to database
db.commit()

# defines variables
id1 = 55
name1 = 'Carl Davis'
grade1 = 61
id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88
id3 = 77
name3 = 'Jane Richards'
grade3 = 78
id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45
id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# list of tuples for rows in table
students_ = [(id1,name1,grade1),(id2,name2,grade2),(id3,name3,grade3),(id4,name4,grade4),(id5,name5,grade5)]

# Inserts students into table called 'python_programming'
cursor.executemany('''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?);''', students_)

# outputs success of updating database
print('Users inserted into table successfully.')

# saves changes to database
db.commit()

# selects records with 60<grade<80
cursor.execute('''SELECT id, name, grade FROM python_programming WHERE grade<? AND grade>?;''', (80, 60))
records = cursor.fetchall()
# returns results
print(records)

# returns to last commit call
db.rollback()

cursor = db.cursor()
# changes Carl Davis's grade to 65
cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ?;''', (65, 'Carl Davis'))
db.commit()

# deletes Dennis Fredrickson's row
name = 'Dennis Fredrickson'
cursor.execute('''DELETE FROM python_programming WHERE name = ?;''', (name,))
# saves changes to database
db.commit()

# changes grade(s) of all people with an id below 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < ?;''', (80, 55))
# saves changes to database
db.commit()

# closes database
db.close()