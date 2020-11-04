# Accessing 2d Array
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
#Input 2d Array
n = int(input()) 
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
#Creating 2d Array

n = 3
m = 4
a = [[0] * m for i in range(n)]
