'''Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

my_list = []
with open("text_1.txt", "w") as file_obj:
    file_obj.writelines(my_list)
while True:
    line = input("Введите произвольную строку: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)
