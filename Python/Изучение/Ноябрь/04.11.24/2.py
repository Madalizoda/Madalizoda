n = int(input("Введите длину словаря: "))
d = {}
print(d)
for i in range(n):
    key = input("Ключ: ")
    value = input("Значение: ")
    d[key] = value
print(d)
