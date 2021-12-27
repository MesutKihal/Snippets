import concurrent.futures


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(pow, 3, 3)
    print(future.result())    
    
