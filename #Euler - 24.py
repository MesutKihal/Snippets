from itertools import permutations 


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 1
for perm in permutations(digits):
    if i == 1000000:
        print(perm)
        break
    i += 1

