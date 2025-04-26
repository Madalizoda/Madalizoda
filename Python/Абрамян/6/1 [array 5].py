a = int(input('Введите целое число > 2: '))
l = list()
l.append(1)
l.append(1)
for i in range(2, a + 1):
    l.append(l[i - 1] + l[i - 2])
print(l)