

def TrianglePS(x1,x2,y1,y2):
    print('Периметр прямоугольника = ', 2*((x2-x1)+(y2-y1)))
    print('Площадь прямоугольника = ', (x2-x1)*(y2-y1))

for i in range(3):
    x1 = int(input("Введите х1: "))
    x2 = int(input('Введите х2: '))
    y1 = int(input('Введите у1: '))
    y2 = int(input('Введите у2: '))
    TrianglePS(x1,x2,y1,y2)