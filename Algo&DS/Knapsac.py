

values = [5, 7, 16, 6, 2, 3]

weights = [2, 5, 1, 4, 8, 6]

def knapsac(target, values, weights, i=0, memo={}):
     key = (target, i)
     if key in memo:
          return memo[key]
     else:
          if i == len(weights):
               memo[key] = 0
               return memo[key]
          else:
               if target <= 0:
                    memo[key] = 0
                    return memo[key]
               else:
                    rsl1 = values[i] + knapsac(target-weights[i], values, weights, i)
                    rsl2 = knapsac(target, values, weights, i=i+1)
                    memo[key] = max(rsl1, rsl2)
                    return memo[key]

print(knapsac(12, values, weights))
