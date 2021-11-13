
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(40)/(factorial(20)*factorial(20)))
