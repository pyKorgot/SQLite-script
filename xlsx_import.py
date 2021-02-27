from openpyxl import load_workbook
import sqlite3


def get_id_users(cursor):
    """Создает заголовок листа excel"""
    cursor.execute('SELECT id FROM users;')
    base_id = cursor.fetchall()
    return base_id


def save_data_sql(data):
    """Получает на входе масив, и заполеняет поле user им"""
    connection = sqlite3.connect('resume.db')
    cursor = connection.cursor()

    base_id = get_id_users(cursor)

    for user in data:
        wrong = False
        for user_id in base_id:
            if user[0] == user_id[0]:
                wrong = True
        if not wrong:
            cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                           user)

    connection.commit()
    connection.close()


def get_xlsx_data():
    """Обращается к файлу resume_export.xlsx
    и возвращает вторую строку в виде массива"""
    wb = load_workbook('resume_import.xlsx')
    ws = wb.active

    data = []
    row_range = ws[f'A2:H{ws.max_row}']

    for row in row_range:
        user = []
        for val in row:
            user.append(val.value)
        data.append(user)
    return data


if __name__ == '__main__':
    save_data_sql(get_xlsx_data())
