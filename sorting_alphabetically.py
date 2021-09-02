
with open("names.txt", "r") as f:
    arr = f.readlines()[0].replace("\"", "").split(",")

def aheadOf(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if ord(a[i]) == ord(b[j]):
            i += 1
            j += 1
        elif ord(a[i]) > ord(b[j]):
            return False
        else:
            return True
    if i == len(a):
        return True
    elif j == len(b):
        return False
    
def merge(left, right):
    i = 0
    j = 0
    arr = []
    while i < len(left) and j < len(right):
        if aheadOf(left[i], right[j]):
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1     
    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
    return arr


def merge_sort(arr):
    mid = len(arr)//2
    if len(arr) == 1:
        return arr
    else:
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

#print(merge_sort(arr))
print(len(arr))
