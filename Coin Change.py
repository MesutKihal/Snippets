#Not my solution

coins = [1, 2, 3]


def coin_change(target, arr, n, memo):
    if target == 0:
        return 1
 
    if target < 0 or n < 0:
        return 0

    key = (n, target)
    
    if key not in memo:
        incl = coin_change(target - arr[n], arr, n, memo)
        excl = coin_change(target, arr, n-1, memo)
        memo[key] = incl + excl

    return memo[key]
print(coin_change(7, coins, len(coins)-1, {}))
