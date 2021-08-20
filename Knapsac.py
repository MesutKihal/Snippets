
values = [5, 7, 16, 6, 2, 3]

weights = [2, 5, 1, 4, 8, 6]

memo = [0 for _ in range(len(values))]
def knapsac(target, weights, values, n, memo):
    if target <= 0 or n <= 0:
        return 0
    else:
        if not n in memo:
            incl = values[n] + knapsac(target-weights[n], weights, values, n, memo)
            excl = 0 + knapsac(target, weights, values, n-1, memo)
            memo[n] = max([incl, excl])
            return memo[n]
        else:
            return memo[n]

print(knapsac(12, weights, values, len(weights)-1, memo))
    
