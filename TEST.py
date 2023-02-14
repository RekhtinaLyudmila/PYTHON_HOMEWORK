my_file = open('teхt_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
try:   
    with open ('teхt_2.txt'):
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")
