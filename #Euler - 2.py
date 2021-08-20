
def fibonacci(x):
    sum_even = 0
    while x < 4000000:
        x = int(round(x * 1.61803398875))
        if x % 2 == 0:
            sum_even += x
    return sum_even

print(fibonacci(1))
