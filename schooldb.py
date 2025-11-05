import sqlite3

# Connect to database
conn = sqlite3.connect('school.db')
c = conn.cursor()

c.execute('''
CREATE TABLE Students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    date_of_birth DATE NOT NULL
)
''')

conn.commit()

# Close connection
c.close()
conn.close()
