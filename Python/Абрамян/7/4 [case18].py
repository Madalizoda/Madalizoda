a = int(input("Введите число в диапозоне 100 - 999: "))
dct1 = {
    10:"Десять",
    11:"Одиннадцать",
    12:"Двенадцать",
    13:"Тринадцать",
    14:"Четырнадцать",
    15:"Пятнадцать",
    16:"Шестнадцать",
    17:"Семнадцать",
    18:"Восемнадцать",
    19:"Девтнадцать",
}
dct2 = {
    1:"Сто",
    2:"Двести",
    3:"Триста",
    4:"Четыреста",
    5:"Пятьсот",
    6:"Шестьсот",
    7:"Семьсот",
    8:"Восемьсот",
    9:"Девятьсот",
}
dct3 = {
    1:"один",
    2:"два",
    3:"три",
    4:"четыре",
    5:"пять",
    6:"шесть",
    7:"семь",
    8:"восемь",
    9:"девять",
}
dct4 = {
    2:"Двадцать",
    3:"Тридцать",
    4:"Сорок",
    5:"Пятьдесять",
    6:"Шестьдесять",
    7:"Семьдесять",
    8:"Восемьдесять",
    9:"Девяносто",
}
if a in range(100,1000):
    if a % 100 and a % 100 == 0:
        print(dct2[a//100])
    elif a % 10 == 0 and a % 100 // 10 in range(2,10):
        print(dct2[a//100], dct4[a % 100 // 10])
    elif a % 10 > 0 and a % 100 // 10 in range(2,10):
        print(dct2[a // 100], dct4[a % 100 // 10], dct3[a % 10])
    elif a % 10 == 0 and a % 100 // 10 == 1:
        print(dct2[a // 100], dct1[a % 100])
    elif a % 10 > 0 and a % 100 // 10 == 1:
        print(dct2[a // 100], dct1[a % 100])
    elif a % 10 == 0 and a % 100 // 10 == 0:
        print(dct2[a // 100], dct3[a % 10])
    elif a % 10 > 0 and a % 100 // 10 == 0:
        print(dct2[a // 100], dct3[a % 10])
else:
    print("Ввели некорректное число")
