import random as r
a = r.randrange(1,100)
print("Компьютер задумал число от 1 до 100")
print("Найдите это число")
n = int(input("Введите число: "))
while n != a:
    if n > a:
        print("Ввели большее число")
    else:
        print("Ввели меньшее число")
    n = int(input("Введите число: "))
print("Вы нашли загаданное число!")
print("a = ", a)
