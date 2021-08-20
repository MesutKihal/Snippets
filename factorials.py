

#Factorial (n!)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(15))
print()
#Super Factorial (n$)
def super_factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n) * super_factorial(n - 1)
        
print(super_factorial(15))
print()
#Hyper Factorial (nH)
def hyper_factorial(n):
    if n == 0:
        return 1
    else:
        return n**n * hyper_factorial(n - 1)

print(hyper_factorial(15))
