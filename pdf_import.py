import fitz

import sql_save_select

pdf_name = './media/resume_import.pdf'


def format_list(list_users):
    """Форматирование текста и создание переменной для записи в бд"""
    new_user = []
    for user in list_users:
        new_user.append(user.split('\n'))

    users = []
    for user in new_user:
        user = [x for x in user if x]
        users.append(user)

    new_user = []
    for user in users:
        list_users = []
        for var in user:
            if user.index(var) == 0:
                var = var.split('№')[1]
                list_users.append(int(var))
                continue
            var = var.split(': ')[1]

            list_users.append(var)
        new_user.append(list_users)

    return new_user


def get_text():
    """Получает текст из пдф файла, с каждой страницы"""
    doc = fitz.open(pdf_name)

    len_doc = doc.page_count

    list_users = []

    for page in range(len_doc):
        load = doc.load_page(page)
        text = load.get_text()
        list_users.append(text)

    return list_users


if __name__ == '__main__':
    sql_save_select.save_data_sql(format_list(get_text()))
