'''Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).'''



words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    word_bytes = word.encode('utf-8')
    print(word_bytes, type(word_bytes))
    word_str = bytes.decode(word_bytes, 'utf-8')
    print(word_str, type(word_str))