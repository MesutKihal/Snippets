import random

arr = [95, 70, 35, 71, 64, 62, 11, 20, 28, 48, 15, 12, 11, 93, 52, 73, 38, 54, 99, 83, 36, 66, 28, 85, 22, 29, 46, 69, 49, 23, 63, 92, 50, 47, 52, 28, 39, 43, 93, 47]


def find_path(start, value, arr, closed=[]):
    if start in closed:
        return 0
    else:
        closed.append(start)
        if start < 0 or start >= 40:
            return 0
        elif arr[start] == value:
            return start
        else:
            return max(find_path(start+1, value, arr), find_path(start-1, value, arr))

print(find_path(0, 66, arr))

