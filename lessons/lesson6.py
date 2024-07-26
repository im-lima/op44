# venv виртуальное окружение
# зависимости
# модули 3 1встроенные 2собвственные 3 внешние

# database
# SQL - язык
# СУБД
# ''
import sqlite3 as sq

with sq.connect('base.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
    fullname TEXT NOT NULL,
    old DATE
)''')
    cursor.execute('''SELECT rowid,fullname,old FROM user  ''')
    print(cursor.fetchall())