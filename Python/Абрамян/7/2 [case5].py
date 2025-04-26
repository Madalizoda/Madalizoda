n = int(input("Введите номер действия: "))
a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
if n == 1:
    print("A + B =", a + b)
elif n == 2:
    print("A - B =", a - b)
elif n == 3:
    print("A * B =", a * b)
elif n == 4:
    print("A / B =", a / b)
else:
    print("Ввели некорректное число")
