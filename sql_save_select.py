import sqlite3

name_database = 'resume.db'


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


def get_sql_data():
    """Получает данные из таблицы users и возвращает их"""
    connect = sqlite3.connect(name_database)
    cursor = connect.cursor()

    cursor.execute("""SELECT u.id, u.second_name, u.first_name, u.patronymic, r.region_name,
                   c.city_name, u.phone, u.email FROM users u LEFT OUTER JOIN
                   regions r ON r.id=u.region_id LEFT OUTER JOIN cities c ON
                   c.id=u.city_id;""")
    data = cursor.fetchall()

    cursor.close()
    return data
