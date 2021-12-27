
def string_reversal(string):
    i = len(string)-1
    if string == "":
        return ""
    else:
        return string[i] + string_reversal(string[:i])

print(string_reversal('HELLO'))

def palindrome(string):
    i = len(string)-1
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        if string[0] == string[i]:
            return palindrome(string[1:i])
        else:
            return False
        
print(palindrome('racecar'))


def binary(num):
    result = num % 2
    if num == 0:
        return "0"
    else:
        return  binary(num // 2) + str(result)
print(binary(233))

arr = [1, 2, 3, 4, 5]

def product(arr, i):
    global j
    if i == len(arr):
        return 1
    else:
        if i != j:
            return arr[i] * product(arr, i+1)
        else:
            return 1 * product(arr, i+1)

prods = []
for j in range(len(arr)):
    prods.append(product(arr, 0))

print(prods)


def sumOf(n):
    if n == 1:
        return 1
    else:
        return n + sumOf(n - 1)

print(sumOf(4))

def LCS(a, b, i, j):
    if i == len(a) or j == len(b):
        return 0
    elif a[i] == b[j]:
        return 1 + LCS(a, b, i+1, j+1)
    else:
        return max([LCS(a, b, i+1, j),LCS(a, b, i, j+1)])

i = 0
j = 0
print(LCS("abdscex", "desx", i, j))


def LIS(l):
    arr = []
    i = 0
    while i < len(l):
        if i == 0:
            arr.append([l[0]])
        else:
            if l[i] > arr[-1][-1]:
                arr[-1].append(l[i])
            elif l[i] > arr[-1][0]:
                arr.append([arr[-1][0], l[i]])
            else:
                arr.append([l[i]])
        i += 1
    return max(list(map(lambda x:len(x), arr)))

print(LIS([4, 3, 8, 6, 7, 0, 1, 8, 7, 2]))

def Subset_Sum(arr, n, subset, i=0):
    if n == 0:
        return True
    elif n < 0:
        return False
    elif i == len(arr):
        return False
    else:
        if Subset_Sum(arr, n-arr[i], subset, i=i+1):
            subset.append(arr[i])
        else:
            Subset_Sum(arr, n, subset, i=i+1)
    return subset

print(Subset_Sum([5, 3, 7, 2, 8], 14, []))


def truncate(arr, removals=0):
    if len(arr) == 1:
        return removals
    elif min(arr)*2 > max(arr) and min(arr) != max(arr):
        return removals
    else:
        rsl1 = truncate(arr[1:], removals+1)
        rsl2 = truncate(arr[:len(arr)-1], removals+1)
        return min(rsl1, rsl2)
print(truncate([9, 7, 9, 2, 3, 8, 1]))

def peak(arr, i=1):
    if i == len(arr):
        return 0
    if arr[i-1] <= arr[i] >= arr[i+1] or (arr[i] >= arr[i+1] and i==0) or (arr[i] <= arr[i-1] and i==len(arr)-1):
        return arr[i]
    else:
        return peak(arr, i+1)
        
print(peak([8, 9, 10, 2, 5, 6]))
