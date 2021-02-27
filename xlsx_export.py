import sqlite3
from openpyxl import Workbook


def get_sql_data():
    """Получает данные из таблицы users и возвращает их"""
    connect = sqlite3.connect('resume.db')
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM users;')
    data = cursor.fetchall()

    cursor.close()

    return data


def create_header(ws):
    headers = ['id', 'second_name', 'first_name', 'patronymic', 'region',
               'city', 'phone', 'email']
    i = 0
    for val in ws['A1:H1'][0]:
        val.value = headers[i]
        i += 1


def save_xlsx_data(data):
    """Получает данные и заносит их в таблицу resume_export"""
    wb = Workbook()
    ws = wb.active

    create_header(ws)

    len_data = len(data) + 1
    row_range = ws[f'A2:H{len_data}']

    for user in data:
        row = data.index(user)
        i = 0
        for val in row_range[row]:
            val.value = user[i]
            i += 1

    wb.save('resume_export.xlsx')


save_xlsx_data(get_sql_data())
