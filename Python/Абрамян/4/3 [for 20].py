import math as m
a = int(input("Введите целое число N: "))
b = 0
n = 1
for i in range(1, a + 1):
    if n <= a:
      b += m.factorial(n)
      n += 1
else:
    print("Результат: ", b)

#while n <= a:
#    b += m.factorial(n)
#    n += 1
#else:
#    print("Результат: ", b)
    
