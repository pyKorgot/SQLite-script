from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import sqlite3


def get_sql_data():
    """Получает данные из таблицы users и возвращает их"""
    connect = sqlite3.connect('resume.db')
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM users;')
    data = cursor.fetchall()

    cursor.close()

    return data


def createPDF(dates):
    canvas = Canvas('Test.pdf', pagesize=A4)
    for data in dates:

        pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
        canvas.setFont('FreeSans', 50)

        canvas.drawString(72, 800, f'Resume User №{data[0]}')

        canvas.setFont('FreeSans', 18)

        canvas.drawString(72, 700, f'First Name: {data[2]}')
        canvas.drawString(72, 650, f'Second Name: {data[1]}')
        canvas.drawString(72, 600, f'Patronymic: {data[3]}')
        canvas.drawString(72, 550, f'Region: {data[4]}')
        canvas.drawString(72, 500, f'City: {data[5]}')
        canvas.drawString(72, 450, f'Phone: {data[6]}')
        canvas.drawString(72, 400, f'Email: {data[7]}')
        canvas.showPage()
    canvas.save()


createPDF(get_sql_data())
