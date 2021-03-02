# import openpyxl
import tkinter as tk

import pdf_export
import pdf_import
import xlsx_export
import xlsx_import
from create_db import create_database


def change_lbl_status(message):
    lbl_status.config(text=message)


def create_db():
    message = create_database()
    change_lbl_status(message)


def import_xlsx():
    xlsx_import.main()
    change_lbl_status('Finally import')


def export_xlsx():
    xlsx_export.main()
    change_lbl_status('Finally export')


def export_pdf():
    pdf_export.main()
    change_lbl_status('Finally export')


def import_pdf():
    pdf_import.main()
    change_lbl_status('Finally import')


window = tk.Tk()
window.geometry('300x300')
window.title('Resume Gui v1.0')
window.resizable(width=False, height=False)

lbl = tk.Label(window, text='Resume Gui', font=('Arial Bold', 31))
lbl.grid(column=0, row=0, columnspan=2)

btn_create = tk.Button(window, text='Создание БД', command=create_db)
btn_create.grid(column=0, row=1, columnspan=2)

btn_x_import = tk.Button(window, text='Импорт из xlsx', command=import_xlsx)
btn_x_import.grid(column=0, row=2)

btn_x_export = tk.Button(window, text='Экспорт в xlsx', command=export_xlsx)
btn_x_export.grid(column=1, row=2)

btn_p_import = tk.Button(window, text='Импорт из PDF', command=import_pdf)
btn_p_import.grid(column=0, row=3)

btn_p_export = tk.Button(window, text='Экспорт в PDF', command=export_pdf)
btn_p_export.grid(column=1, row=3)

lbl_status = tk.Label(window, text='', font=('Arial Bold', 14))
lbl_status.grid(column=0, row=4, columnspan=2)
window.mainloop()
