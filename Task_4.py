# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# from math import pi
# p = pi
# d = float(input("Введите число для заданной точности числа Пи: "))
# if d ==1:
#     print(int(p))
# else:
#     d = str(d)
#     d = d.split('.')
#     d = len(d[1])
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')






# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input("Введите число:  "))
# i = 2
# Ist = []
# old = n
# while i<=n:
#     if n % i == 0:
#         Ist.append(i)
#         n //= i
#         i = 2
#     else:
#         i +=1
# print(f'Простые множители числа {old} приедены в списке: {Ist}')




# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

# Ist = list(map(int, input("Введите числа через пробел: \n").split()))
# print(f'Исходный список: {Ist}')
# new_Ist = []
# for i in Ist:
#     if Ist.count(i)==1:
#         new_Ist.append(i)
# print(f'Список из неповторяющихся элементов: {new_Ist}')





# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
#
# some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
# k = int(input('Введите натуральную степень k: '))
# coef = [random.randint(0, 100) for _ in range(k + 1)]
# print(coef)
# with open('coef.txt', 'w', encoding='utf-8') as m:
#     for i in range(len(coef)):
#         if k - i != 1 and k - i != 0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')











# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


# with open('my_1.txt', 'w',encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('my_2.txt', 'w',encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')
#
# with open('my_1.txt', 'r') as file:
#     my_1 = file.readline()
#     list_of_my_1 = my_1.split()
#
# with open('my_2.txt', 'r') as file:
#     my_2 = file.readline()
#     list_of_my_2 = my_2.split()
#
# print(f'{list_of_my_1} + {list_of_my_2}')
# sum_my = list_of_my_1 + list_of_my_2
#
# with open('sum_my.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_my_1} + {list_of_my_2}')










