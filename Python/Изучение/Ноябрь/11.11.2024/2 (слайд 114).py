import math as m
def my_func( a, b, c ):
    p = (a + b + c)/2
    s = m.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print(my_func(a,b,c))