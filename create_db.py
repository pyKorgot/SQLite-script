from os import path
import sqlite3
from sqlite3 import Error


def insert_database(cursor):
    """Заполняет базу данных из скрипта create.sql"""
    sql_file = open('create.sql').read()

    cursor.executescript(sql_file)


def create_database():
    """Создает Базу данных если ее нет в папке,
    и передает подключение для заполнения"""
    if not path.exists('resume.db'):
        try:
            con = sqlite3.connect('resume.db')
            insert_database(con.cursor())
            con.close()
            print('Connection is established.')

        except Error:
            print(Error)

    else:
        print('Database already exists')


if __name__ == '__main__':
    """Парамметры при запуске"""
    create_database()
