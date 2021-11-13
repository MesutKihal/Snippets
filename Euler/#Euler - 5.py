import concurrent.futures


one_twenty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

num1 = 1


def div(num2):
    global num1
    
    if num1 % num2 == 0:
        return True
    else:
        return False


with concurrent.futures.ThreadPoolExecutor() as executor:

    while True:
        futures = executor.map(div, one_twenty)
        if all([rsl for rsl in futures]):
            print(num1)
            break
        num1 += 1



