import concurrent.futures


one_hundred = [num for num in range(1,101)]


f = lambda x:x**2

with concurrent.futures.ThreadPoolExecutor() as executor:
    
    squares = executor.map(f, one_hundred)
    print(abs(sum(list(squares))-sum(one_hundred)**2))
    
