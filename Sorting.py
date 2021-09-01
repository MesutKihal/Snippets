#   O(n)
def selection_sort(arr):
    i = 0
    while i < len(arr):
        min_index = arr[i:].index(min(arr[i:]))+i
        arr[i], arr[min_index] = arr[min_index], arr[i]
        i += 1
    return arr

print(selection_sort([2, 7, 4, 1, 5, 3]))
#   O(n^2)
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        swaps = 0
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
        if swaps == 0:
            break
    return arr

print(bubble_sort([2, 7, 4, 1, 5, 3]))
#   O(n^2)
def insertion_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        if len(sorted_arr) == 0:
            sorted_arr.append(arr[i])
        elif len(sorted_arr) == 1:
            if arr[i] <= sorted_arr[0]:
                sorted_arr.insert(0, arr[i])
            else:
                sorted_arr.append(arr[i])
        else:
            for j in range(len(sorted_arr)-1):
                if arr[i] < sorted_arr[0]:
                    sorted_arr.insert(0, arr[i])
                    break
                elif arr[i] > sorted_arr[-1]:
                    sorted_arr.append(arr[i])
                    break
                elif sorted_arr[j] <= arr[i] < sorted_arr[j+1]:
                    sorted_arr.insert(j+1, arr[i])
                    break
    return sorted_arr

print(insertion_sort([2, 7, 4, 1, 5, 3]))
#   O(nlogn)
def merge(left, right):
    i = 0
    j = 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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

print(merge_sort([2, 7, 4, 1, 5, 3]))
