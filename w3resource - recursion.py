

#Exercice 1

def sum_list(arr, i):
    if i == len(arr)-1:
        return arr[-1]
    else:
        return arr[i] + sum_list(arr, i=i+1)
    
print(sum_list([2,8,1,3], 0))

#Exercice 3

def sum_arr(arr, i):
    if i < len(arr) and type(arr[i]) == int:
        if i == len(arr)-1:
            return arr[-1]
        else:
            return arr[i] + sum_arr(arr, i=i+1)
    else:
        j = 0
        if i == len(arr)-1:
            return sum_arr(arr[i], j)
        else:
            return sum_arr(arr[i], j) + sum_arr(arr, i=i+1)

print(sum_arr([1, 2, [3,4], [5,6]], 0))

#Exercice 4

facts = [None for _ in range(100)]
def factorial(n):
    if facts[n] != None:
        return facts[n]
    else:
        if n == 0:
            return 1
        else:
            facts[n] = n
            return n * factorial(n-1)
        
print(factorial(80))

#Exercice 5

fibs = [None for _ in range(10000)]

def fibonacci(n):
    if fibs[n] != None:
        return fibs[n]
    else:
        if n == 1 or n == 2:
            return 1
        else:
            fibs[n] = fibonacci(n-1) + fibonacci(n-2)
            return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(100))

#Exercice 6

def sumDigits(number, i):
    if i == len(str(number))-1:
        return int(str(number)[-1])
    else:
        return int(str(number)[i]) + sumDigits(number, i=i+1)

print(sumDigits(345, 0))

#Exercice 7

def sum_series(n):
    try:
        assert n >= 2
        if n == 2:
            return 2
        else:
            return n + sum_series(n-2)
    except AssertionError:
        return None
    
print(sum_series(10))

#Exercice 8

i = 0
def harmonic(n):
    global i
    if i == n-1:
        return 0
    else:
        i = i+1
        return (1/i) + harmonic(n)

print(harmonic(6))

#Exercice 10

i = 0
def power(a, b):
    global i
    if b == 0:
        return 1
    elif i == b-1:
        return a
    else:
        i = i+1
        return a * power(a, b)
    
print(power(3, 4))

#Exercice 11

i = 2
maxi = 1
def gcd(a, b):
    global i, maxi
    try:
        assert a > b
        if i == b//2:
            return maxi
        elif a % i == 0 and b % i == 0:
            if i > maxi:
                maxi = i
            i = i+1
            return gcd(a, b)
        else:
            i = i+1
            return gcd(a, b)
    except AssertionError:
        return gcd(b, a)
    
print(gcd(150, 6500))

