def simple_interest(p,r,t):
    A = p * (1 + ((r / 100)*t))
    return '\nAfter ' + str(t) + ' years at ' + str(r) + '%' ', the investment will be worth ' '$' + str(int(A)) + '.'


result = simple_interest(int(input("Enter the principal: ")),
                         float(input("Enter the rate of interest: ")),
                         int(input("Enter the number of years: ")))
print(result)
