'''Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.'''

words = [b'class', b'function', b'method']

for word in words:
    print('тип переменной: {}\n'.format(type(word)))
    print('содержание переменной - {}\n'.format(word))
    print('длинна строки: {}\n'.format(len(word)))