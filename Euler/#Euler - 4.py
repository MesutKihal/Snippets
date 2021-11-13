import concurrent.futures

num1 = 100


digit = [num for num in range(100, 1000)]

maxi = 0

def palindrome(num2):
    global num1, maxi, a, b
    if str(num1 * num2) == str(num1 * num2)[::-1]:
        if num1 * num2 > maxi:
            maxi = num1 * num2
        return True
    else:
        return False


with concurrent.futures.ThreadPoolExecutor() as executor:
    
    while num1 < 1000:
        futures = executor.map(palindrome, digit)
        num1 += 1
    

print(maxi)

