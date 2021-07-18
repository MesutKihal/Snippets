import concurrent.futures

num1 = 2

divisors = [num for num in range(2, num1)]

def divisble(num2):
    global num1
    if num1 % num2 == 0:
        return True
    else:
        return False



prime = 0

with concurrent.futures.ThreadPoolExecutor() as executor:

    while prime < 120:
        divisors = [num for num in range(2, num1)]
        results = executor.map(divisble, divisors)
        if any(list(results)) == False:
            prime += 1
            print(num1)
        num1 += 1
    
    
