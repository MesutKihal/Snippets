import time
import datetime

#DP Solution
begin = time.time()
fibs = {}
def fibonacci_dp(n):
    if n in fibs:
        return fibs[n]
    else:
        if n == 1 or n == 2:
            return 1
        else:
            fibs[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)
            return fibs[n]
        
print("DP Solution:\t\t"+str(fibonacci_dp(20)))
end = time.time()
print("Time Elapsed:\t\t"+str(datetime.timedelta(seconds=end-begin)))
print()

#Recursive Solution
begin = time.time()
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Recursive Solution:\t"+str(fibonacci(20)))
end = time.time()
print("Time Elapsed:\t\t"+str(datetime.timedelta(seconds=end-begin)))

