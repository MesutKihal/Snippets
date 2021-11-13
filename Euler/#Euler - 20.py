


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(sum([int(char) for char in str(factorial(100))]))
