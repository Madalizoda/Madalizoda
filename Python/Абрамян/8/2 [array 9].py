n = int(input('Введите размер массива: '))
m = []
k = 0
for i in range(1, n+1):
    a = int(input('Введите число: '))
    if a % 2  == 0:
        k += 1
        m.append(a)
print('Все нечетные числа содержащиеся в данном массиве: ', m[::-1])
print('Количество нечетных чисел в данном массиве: ', k)