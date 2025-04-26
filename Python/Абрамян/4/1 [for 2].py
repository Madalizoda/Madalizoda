a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
n = 0
for i in range(a, b+1):
    print(i)
    n += 1
print("Количсетво чисел между ", a, "и", b, ":",n)
