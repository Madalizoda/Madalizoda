import math as m

def TrianglePS(a):
    p = 3*a
    s = m.pow(a,2) * m.sqrt(3/4)
    print("Периметр треуголльника =", p, 'Площадь треуголника =', s)
for i in range(3):
    a = int(input('Введите сторону треугольника: '))
    TrianglePS(a)