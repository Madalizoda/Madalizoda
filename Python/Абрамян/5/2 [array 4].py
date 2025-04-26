n = int(input("Введите целое число( > 1 ): "))
l = []
a = int(input("Введите первый член прогрессии: "))
D = int(input('Введите знаменатель прогрессии: '))
d = D
l.append(a)
for i in range(1,n):
    l.append(a*d)
    d *= D
else:
    print(l)
