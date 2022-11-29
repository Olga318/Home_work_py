import csv
import os.path
import view

def find_ID(ID):
    if os.path.exists("Log_book.csv"):
        with open("Log_book.csv", "r", encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(";"))
            count = 0
            for item in sum_list:
                if ID == item[0]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f"Работник с {ID} не найден!")
    else:
        view.answer("Файл не найден!")

def find_surname(surname):
    if os.path.exists("Log_book.csv"):
        with open("Log_book.csv", "r", encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(";"))
            count = 0
            for item in sum_list:
                if surname == item[1]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f"Работник по фамилии {surname} не найден!")
    else:
        view.answer("Файл не найден!")

def find_name(name):
    if os.path.exists("Log_book.csv"):
        with open('Log_book.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(";"))
            count = 0
            for item in sum_list:
                if name == item[2]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f"Работник по имени {name} не найден!")
    else:
        view.answer("Файл не найден!")

def find_occupation(occupation):
    if os.path.exists("Log_book.csv"):
        with open("Log_book.csv", "r", encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(";"))
            count = 0
            for item in sum_list:
                if occupation == item[6]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f"Работник на должности {occupation} не найден!")
    else:
        view.answer("Файл не найден!")
