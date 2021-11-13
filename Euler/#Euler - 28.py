import numpy

arr = numpy.arange(1,1002002)

diagonals = 1
i = 2
temp = 0

while i < 1001:
    for _ in range(4):
        temp += i
        diagonals += arr[temp]
        
    i += 2

print(diagonals)
