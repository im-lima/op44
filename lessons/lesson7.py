import sqlite3 as sql
# СУБД
# sql
# CRUD - create read U|D
with sql.connect('base.db') as connection:
    cursor = connection.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS gamers''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS gamers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age INTEGER DEFAULT 1
    )''')
    # INSERT вставить
    # INTO выборка
    # cursor.execute('''INSERT INTO gamers (name,age)
    # VALUES
    # ('beka',20),
    # ('bekbolot',69),
    # ('beka1',21),
    # ('beka',0),
    # ('beka',29),
    # ('akeb',50),
    # ('aidar',20)
    #  ''')
    # cursor.execute('''INSERT INTO gamers (name,age) VALUES ('jjj',9) ''')

    cursor.execute('''DELETE FROM gamers WHERE id>20''')

    cursor.execute('''UPDATE gamers SET name ="old" WHERE age > 30''')

    cursor.execute('''SELECT * FROM gamers WHERE age BETWEEN 18 AND 49''')
    # for i in cursor.fetchall():
    #     print(i)

    cursor.execute('''SELECT * FROM gamers ORDER BY id''')
    # n=[(),(),(),(),(),(),(),(),(),()]
    for i in cursor.fetchall():
        print(i)