l = ['один', 'два', 'три', 'четыре', 'пять']
l2 = []
f1 = open('Lesson8/text_3.txt')
a = f1.readlines()
print(a)
e = len(a)
j = 0
for i in a:
    b = i
    c = i.find(' ')
    d = i[:c]
    r = b.replace(d, l[j])
    j = j + 1
l2.append(r)
f2 = open('text_3_new.txt', 'w')
f2.writelines(l2)