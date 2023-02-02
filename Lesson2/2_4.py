'''Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3
Введите целые числа через пробел: 1 2 3
Результат: 2 1 3'''

el_count = input("Введите целые числа через пробел: ")
my_list = (el_count.split())

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1] 
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)


'''el_count = int(input("Введите целые числа через пробел: "))
el = el_count.split(", ")
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("el_count"))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)'''
