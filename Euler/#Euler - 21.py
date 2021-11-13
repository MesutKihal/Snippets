from functools import reduce


def factors(n):
    return sum(set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))-n

def amicable(a):
    b = factors(a)
    if a == factors(b) and a != b:
        return True
    else:
        False

sum_amicable = 0

i = 2

while i < 10000:
    if amicable(i):
        sum_amicable += i
    i += 1

print(sum_amicable)
