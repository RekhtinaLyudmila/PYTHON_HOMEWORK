'''Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).'''

class ErrorByByte(Exception):
    def __init__(self, err):
        self.err = err


words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    word_b = bytes(word, 'ascii', 'ignore')
    try:
        if word_b == b'':
            raise ErrorByByte(
                f'{word}  - невозможно записать в байтовом типе')
        print(word_b)
    except ErrorByByte as err:
        print(err)

