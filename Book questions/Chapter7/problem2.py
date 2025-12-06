import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

name = input("Enter name: ")
grade = float(input("Enter grade: "))

cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
conn.commit()

cursor.execute('SELECT * FROM students')
print("--- Updated Records ---")
for row in cursor.fetchall():
    print(row)

conn.close()