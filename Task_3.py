# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих
# на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



def sum_odd_index(Ist):
    s = 0
    for i in range(len(Ist)):
        if i % 2 != 0:
            s += Ist[i]
    print(f'Сумма равна: {s}')

# Ist = [2, 3, 4, 6, 9]
# sum_odd_index(Ist)

Ist = list(map(int, input('Введите числа через пробел: \n').split()))
sum_odd_index(Ist)




# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint
#
# number = int(input('Введите размер списка: '))
# list = []
# list2 = []
#
# for i in range(number):
#     list.append(randint(1, 9))
#
# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1
# print(list)
# print(list2)






# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# some_list = list(map(float, input("Введите числа через пробел: \n").split()))
# min = 1
# max = 0
# for i in some_list:
#     if(i - int(i)) <= min:
#         min = i - int(i)
#     if(i - int(i)) >= max:
#         max = i - int(i)
# dif = round((max - min), 2)
# print(dif)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#
# n = int(input("Введите число: "))
# bin = ""
# while n > 0:
#     bin = str(n % 2) + bin
#     n //= 2
# print(f"Бинарное число {bin}")





# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n - 2)
#
#
# def nega_fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2
#
#
# list = [0]
# number = int(input("Введите число: "))
# for e in range(1, number + 1):
#     list.append(fib(e))
#     list.insert(0, nega_fib(e))
# print(list)

