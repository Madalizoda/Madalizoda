def AddRightDigit(k):
    d1 = str(input('Введите первое число (d1): '))
    k += d1
    print(k)
    d2 = str(input('Введите второе число (d2): '))
    k += d2
    print(k)
k = str(input('Введите целое число (k): '))
AddRightDigit(k)