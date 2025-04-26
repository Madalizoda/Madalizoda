a = {"a", "b", 'c'}
b = {'f', 'd', 'a'}

x = a.union(b)
print(x)
y = a|b
print(y)

x= a.intersection(b)
print(x)
y = a & b
print(y)

x = a.difference(b)
print(x)
y = a - b
print(y)


x = b.difference(a)
print(x)
y = b - a
print(y)
