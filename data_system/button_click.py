import export_data as exp
import import_data as imp
import view
import log

def button_click():
    choise = view.button()
    while choise != "q":
        log.log_info(choise)
        if choise == "1":
            exp.export_data()
        elif choise == "2":
            what_find = input("Для поиска по номеру ID введите '1'\nДля поиска по фамилии введите '2'\n Для поиска по имени введите '3'\nДля поиска по должности введите '4'\n ")
            if what_find == '1':
                imp.find_ID(input('номер ID: '))
            if what_find == '2':
                imp.find_surname(input('Введите фамилию: '))
            if what_find == '3':
                imp.find_name(input('Введите имя: '))
            if what_find == '4':
                imp.find_occupation(input('Введите должность: '))
        else:
            print("Такой команды нет")
        choise = view.button()
