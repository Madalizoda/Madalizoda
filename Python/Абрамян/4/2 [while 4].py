a = int(input("Введите целое число: "))
if a <= 0:
    print("Число является степенью 3: FALSE")
else:
    while a % 3 == 0:
        a //= 3
    if a == 1:
        print("Число является степенью 3: TRUE")
    else:
        print("Число является степенью 3: FALSE")


