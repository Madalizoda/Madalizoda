import math as m
def my_function(a):
    x = m.fabs(a)
    y = m.sqrt(x)
    y = m.exp(m.sin(y) + 1)
    return y
print(my_function(2))