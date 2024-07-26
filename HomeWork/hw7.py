import sqlite3 as sql

with sql.connect('students.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hobby TEXT,
        first_name TEXT,
        last_name TEXT,
        birth_year INTEGER,
        hw_points INTEGER
    )''')

    cursor.execute('''INSERT INTO student (hobby, first_name, last_name, birth_year, hw_points) VALUES
        ('Football', 'Johnny', 'Depp', 2000, 29),
        ('Reading', 'Jim', 'Carrey', 2002, 30),
        ('Music', 'Robert', 'Downey Jr.', 2001, 15),
        ('Drawing', 'Leonardo', 'DiCaprio', 2004, 40),
        ('Sports', 'Ryan', 'Gosling', 2007, 56),
        ('Programming', 'Emma', 'Watson', 2006, 60),
        ('Swimming', 'Daniel', 'Radcliffe', 2004, 49),
        ('Languages', 'Brad', 'Pitt', 2000, 30),
        ('Traveling', 'Will', 'Smith', 2005, 5),
        ('Photography', 'Arnold', 'Schwarzengger', 2003, 10)
    ''')

    cursor.execute('''SELECT * FROM student WHERE LENGTH(last_name) > 10''')
    students_with_long_last_name = cursor.fetchall()
    print("Students with last name longer than 10 characters:")
    for student in students_with_long_last_name:
        print(student)

    cursor.execute('''UPDATE student SET first_name = 'genius' WHERE hw_points > 10''')

    cursor.execute('''SELECT * FROM student WHERE first_name = 'genius' ''')
    genius_students = cursor.fetchall()
    print("\nStudents with first name 'genius':")
    for student in genius_students:
        print(student)

    cursor.execute('''DELETE FROM student WHERE id % 2 = 0''')

    cursor.execute('''SELECT * FROM student ORDER BY id''')
    remaining_students = cursor.fetchall()
    print("\nRemaining students:")
    for student in remaining_students:
        print(student)