import sqlite3

name_database = 'resume.db'


def format_data(data, cursor):
    """Привязывает строковое представление для импорта в виде INT ключа"""
    cursor.execute('SELECT * FROM regions;')
    regions = cursor.fetchall()
    for region in regions:
        if data[4] == region[1]:
            data[4] = region[0]

    cursor.execute('SELECT * FROM cities;')
    cities = cursor.fetchall()
    for citie in cities:
        if data[5] == citie[2]:
            data[5] = citie[0]

    return data


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
    format_data(data, cursor)

    for user in data:
        if isinstance(user[4], str) or isinstance(user[5], str):
            data = format_data(user, cursor)

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
