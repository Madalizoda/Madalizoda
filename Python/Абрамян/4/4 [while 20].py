a = int(input("Введите целое число: "))
if a > 0:
    b = 0
    while a > 0:
        n = a % 10
        if n == 2:
            print("TRUE")
            b = 1
            break 
        a = a // 10
    if b == 0:
        print("FALSE")

    
