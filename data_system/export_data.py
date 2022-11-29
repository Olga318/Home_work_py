import os.path
import csv


def export_data():
    if not os.path.exists("Log_book.csv"):
        with open("Log_book.csv", "w", encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=";")
            writer.writerow(("ID", "Фамилия", "Имя", "отчество", "Номер телефона", "адрес", "должность"))
    exit = ""
    while exit != "q":
        user_data = [
            input('введите ID-номер: '),
            input('введите фамилию: '),
            input('введите имя: '),
            input('введите отчество: '),
            input('введите номер телефона: '),
            input('введите адрес: '),
            input('введите должность: ')
        ]
        with open('Log_book.csv', 'a', encoding='utf-8') as dt:
            dt.write(f'{user_data[0]};{user_data[1]};{user_data[2]};{user_data[3]};{user_data[4]};{user_data[5]};{user_data[6]}\n')

        with open('Log_book.txt', 'a', encoding='utf-8') as dt:
            dt.write(f' ID: {user_data[0]}\nФамилия: {user_data[1]}\nИмя: {user_data[2]}\nОтчество: {user_data[3]}\nНомер телефона: {user_data[4]}\nАдрес: {user_data[5]}\nДолжность: {user_data[6]}\n\n\n')

        exit = input('Создана новая запись в телефонной книге.\n\nДля выхода из телефонной книги нажмите "q"\n Для продолжения нажмите "Enter"\n')
