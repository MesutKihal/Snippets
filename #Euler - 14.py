def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


def collatz(num):
    if isEven(num):
        yield num//2
    else:
        yield 3*num + 1

num = 1
maxi = (0,0)
while num < 1000000:
    temp = num
    terms = 1
    while temp != 1:
        temp = next(collatz(temp))
        terms += 1
    if terms > maxi[1]:
        maxi = (num, terms)
    num += 1
    
print(maxi)
