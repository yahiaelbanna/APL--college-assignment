import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

try:
    conn.execute('BEGIN')
    
    new_students = [
        ('Ahmed', 88.0),
        ('Fatima', 91.5)
    ]
    cursor.executemany('INSERT INTO students (name, grade) VALUES (?, ?)', new_students)
    
    result = 1 / 0

    conn.commit()
    print("Transaction committed successfully")
    
except ZeroDivisionError as e:
    conn.rollback()
    print(f"Error occurred: {e}")
    print("Transaction rolled back")
    
    cursor.execute('SELECT * FROM students')
    print("Final Records:")
    for row in cursor.fetchall():
        print(row)
        
finally:
    conn.close()