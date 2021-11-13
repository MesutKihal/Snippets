import numpy
from functools import reduce

def factors(n):    
    return len(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def triangle_number(i):
    return sum(numpy.arange(1, i+1))

i = 1
temp = 1

while factors(temp) < 500:
    temp = triangle_number(i)
    i += 1

print(temp)
