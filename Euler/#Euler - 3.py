import math

def prime(x):
    try:
        assert x > 1
        i = 2
        isPrime = True
        while i <= int(math.floor(math.sqrt(x))):
            if prime(i):
                if x % i == 0:
                    isPrime = False
                    break
                else:
                    isPrime = True
            i += 1
        return isPrime
    except AssertionError:
        return False


maxi = 0

num = 600851475143

i = 0

while i < int(math.floor(math.sqrt(num))):
    if prime(i):
       if num % i == 0:
           if i > maxi:
               maxi = i
    i += 1
print(maxi)


