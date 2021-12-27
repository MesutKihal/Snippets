
combins = []

def find_arrangements(r, g, b, memo, comb=""):
     key = (r, g, b, comb)
     if key in memo:
          return memo[key]
     else:
          if r < 0 or g < 0 or b < 0:
               memo[key] = ""
               return memo[key]
          
          if r == 0 and g == 0 and b == 0:
               memo[key] = comb
               return memo[key]
          else:
               if comb == "":
                    rsl1 = find_arrangements(r-1, g, b, memo, comb=comb+"r")
                    rsl2 = find_arrangements(r, g-1, b, memo, comb=comb+"g")
                    rsl3 = find_arrangements(r, g, b-1, memo, comb=comb+"b")
                    for rsl in [rsl1, rsl2, rsl3]:
                         if rsl != "" and rsl != None:
                              combins.append(rsl)
               else:
                    if comb[-1] == "r":
                         rsl1 = find_arrangements(r, g-1, b, memo, comb=comb+"g")
                         rsl2 = find_arrangements(r, g, b-1, memo, comb=comb+"b")
                         for rsl in [rsl1, rsl2]:
                              if rsl != "" and rsl != None:
                                   combins.append(rsl)
                    if comb[-1] == "g":
                         rsl1 = find_arrangements(r-1, g, b, memo, comb=comb+"r")
                         rsl2 = find_arrangements(r, g, b-1, memo, comb=comb+"b")
                         for rsl in [rsl1, rsl2]:
                              if rsl != "" and rsl != None:
                                   combins.append(rsl)
                    if comb[-1] == "b":
                         rsl1 = find_arrangements(r-1, g, b, memo, comb=comb+"r")
                         rsl2 = find_arrangements(r, g-1, b, memo, comb=comb+"g")
                         for rsl in [rsl1, rsl2]:
                              if rsl != "" and rsl != None:
                                   combins.append(rsl)
                         

find_arrangements(3, 1, 2, {})
print(combins)
