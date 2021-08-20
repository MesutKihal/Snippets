import math

num1 = 2

def prime(x):
    try:
        assert x > 1
        i = 2
        isPrime = True
        while i <= int(math.floor(math.sqrt(x))):
            if x % i == 0:
               isPrime = False
               break
            else:
                isPrime = True
            i += 1
        return isPrime
    except AssertionError:
        return False



primes = 0


while primes < 10001:
    if prime(num1):
        primes += 1
    num1 += 1

print(num1-1)
   
