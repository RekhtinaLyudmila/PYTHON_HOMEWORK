'''Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
'''

s = input("Введите операцию (0, +, -, *, /,): ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
  
if s == "+":
     print("%.2f" % (a+b))
elif s == '-':
    print("%.2f" % (a-b))
elif s == '*':
    print("%.2f" % (a*b))
elif s == '/':
    if b != 0:
        print("%.2f" % (a/b))
else:
    print("Деление на ноль!")

while True:
    if s == '0': break   

print("Ноль в качестве знака операции завершит работу программы")