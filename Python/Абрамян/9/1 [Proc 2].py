import math as m
def powera234(a):
    b = a*a
    c = b*a
    d = c*a
    return b, c, d

a = int(input('Введите число: '))
print(powera234(a))