#1
for i in [1,2,5,4]:
    print(i)
else:
    print("Цикл завершен")


print("====================")
#2
for i in range(1,10):
    print(i)
else:
    print("Цикл завершен")

print("============================================")
#3
for i in range(20,101,20):
    print(i)
else:
    print("Цикл завершен")

print("=======================================")
#4

for i in range(100, 19, -20):
    print(i)
else:
    print("Цикл завершен")

print("====================")
#5
for i in 'abcd':
    print(i, end = " ")

print("   ")

#6
for i in range(1,11):
    if i % 2 == 0:
        print(i, end = " ")
