import sqlite3

conn = sqlite3.connect('person.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments (DepartmentID)
)
''')

departments = [
    (101, 'HR'),
    (102, 'IT'),
    (103, 'Sales')
]
cursor.executemany('INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (?, ?)', departments)

employees = [
    (1, 'Al', 'Pacino', 101),
    (2, 'Russell', 'Crowe', 101),
    (3, 'Charles', 'Chaplin', 102),
    (4, 'Kate', 'Winslet', 102),
    (5, 'Mark', 'Wahlberg', 103),
    (6, 'Natalie', 'Portman', 103)
]
cursor.executemany('INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID) VALUES (?, ?, ?, ?)', employees)

conn.commit()

cursor.execute('''
SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
''')

all_employees = cursor.fetchall()
print("Все сотрудники с указанием их отделов:")
for employee in all_employees:
    print(employee)

cursor.execute('''
SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'IT'
''')

it_employees = cursor.fetchall()
print("\nСотрудники отдела IT:")
for employee in it_employees:
    print(employee)

conn.close()