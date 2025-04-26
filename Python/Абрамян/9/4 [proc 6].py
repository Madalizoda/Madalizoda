def DigitCountSum(c):
    C = c
    a = 0
    c = str(c)
    print('Количество цифр =',len(c) )
    for i in range(len(c)):
        a += int(c) % 10
        c = c[:-1]


    print('Сумма цифр = ', a)

for i in range(5):
    c = int(input('Введите число: '))
    DigitCountSum(c)