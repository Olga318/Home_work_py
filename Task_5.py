#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# def x(i):
#     return "абв" not in i
#
# text = input("Введите текст: ")
# text = text.split()
#
# text2 = list(filter(x, text))
#
# print(text2)



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file.text', 'w', encoding='UTF-8') as file:
    file.write('wwwwwwwwwwwwwwwwddrrrrrrrrrrrrrrrffftsssssssssssssss')
with open('file.text', 'r', encoding='UTF-8') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()

print(my_txt)


def file_encond(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''
    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compr = file_encond(my_txt)

with open('file_decode.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)
print(f'Compress ratio:\t{round(len(my_txt) / len(txt_compr), 1)}')


