from functools import reduce


def factors(n):
    return sum(set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

i = 2

sum_primes = 0

while i < 2000000:
    if factors(i) == i+1:
        sum_primes += i
    i += 1
        
print(sum_primes)
    
