import math as m

def TriangleP(a,h):
    b = m.sqrt(pow((a/2),2)+h*h)
    print('Периметр треугольника равен', 2*b + a)
for i in range(3):
    a = int(input('Введите основание треугольника: '))
    h = int(input('Введите высоту треугольника: '))
    i += 1
    TriangleP(a,h)
