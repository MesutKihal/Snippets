

arr = [5, 2, 8, 6, 7, 4, 5, 9, 10 , 0]


indexes = list(enumerate(arr))
maximum = list(filter(lambda x:x[1]>arr[j], indexes))

def LIS(arr, i, j):
    result = 1
    
    if i == len(arr):
        result = result
    else:
        if arr[i] > arr[j]:
            j = i
            return 1 + LIS(arr, i+1, j)
        else:
            return 0 + LIS(arr, i+1, j)

    return result

print(LIS(arr, 0, 0))




