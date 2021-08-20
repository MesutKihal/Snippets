from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def abundant(n):
    if sum(factors(n))-n > n:
        return True
    else:
        return False

i = 1

while i < 28123:
    pass
    i += 1
