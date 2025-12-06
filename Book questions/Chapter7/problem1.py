import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade REAL
)
''')

students = [
    ('Ali', 85.5),
    ('Sara', 92.0),
    ('Mohamed', 78.3)
]

cursor.executemany('INSERT INTO students (name, grade) VALUES (?, ?)', students)
conn.commit()

cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(row)

conn.close()