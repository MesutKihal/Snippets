import concurrent.futures
import math

nums = [num for num in range(1,1000)]

b = 1

def triplet(a):
    global b
    c = math.sqrt(a**2 + b**2)
    
    if a**2 + b**2 == c**2 and a < b < c and a + b + c == 1000:
        return True
    else:
        return False


with concurrent.futures.ThreadPoolExecutor() as executor:

    while b < 1000:
        
        results = executor.map(triplet, nums)
        try:
            a = nums[list(results).index(True)]
            print(a*b*math.sqrt(b**2+a**2))
            break
        except ValueError:
            pass
        b += 1

