import sqlite3
from os import path
from sqlite3 import Error

name_database = 'resume.db'


def insert_database(cursor):
    """Заполняет базу данных из скрипта create.sql"""
    sql_file = open('create.sql').read()

    cursor.executescript(sql_file)


def create_database():
    """Создает Базу данных если ее нет в папке,
    и передает подключение для заполнения"""
    if not path.exists(name_database):
        try:
            con = sqlite3.connect(name_database)
            insert_database(con.cursor())
            con.close()
            message = 'Connection is established.'
            print(message)
            return message

        except Error:
            print(Error)

    else:
        message = 'Database already exists'
        print(message)
        return message


if __name__ == '__main__':
    """Парамметры при запуске"""
    create_database()
