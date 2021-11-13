
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_change(target, index=0, memo={}):
     key = (target, index)
     if key in memo:
          return memo[key]
     else:
          if index == len(coins):
               memo[key] = 0
               return memo[key]
          elif target < 0:
               memo[key] = 0
               return memo[key]
          elif target == 0:
               memo[key] = 1
               return memo[key]
          else:
               memo[key] = coin_change(target-coins[index], index) + coin_change(target, index+1)
               return memo[key]

print(coin_change(200))
