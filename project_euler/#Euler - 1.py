

def multiples(x):
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False

sum_multi = 0

i = 0
while i < 1000:
    if multiples(i):
        sum_multi += i
    i += 1
      
print(sum_multi)



