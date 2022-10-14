# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# x = input('Введите число: ')
# def summa(x):
#     if float(x) < 0:
#         x = float(x) * -1
#     number = 0
#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number
#
# print (f'Сумма чисел равна {summa(x)}')


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# x = int(input('Введите число: '))
# factorial = 1
# print('[ ', end='')
# for i in range(1, x+1):
#     factorial *= i
#     print(factorial, end=' ')
# print(']')



# Задайте список из n чисел последовательности (1+1/ n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44} сумма: 9,06

# n = int(input('Введите число: '))
# def sequence(n):
#     return[round((1+1/x)**x, 2) for x in range(1, n+1)]
#
# print(sequence(n))
# print(round(sum(sequence(n)), 2))



# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# n = int(input('Введите число: '))
# import random
#
# randlist = random.sample(range(-n, n), n)
# print(randlist)
#
# data = open('file.txt', 'w')
# data.writelines(positions)
# data.close()
           # программа не дописана







# Реализуйте алгоритм перемешивания списка.

#import random

# example = list('abracadabra')
# print(example)
# random.shuffle(example)
# print(example)




