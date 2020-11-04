def simple_interest_compound(p,r,t,n):
    A = p * (1 + (r / 100) / n) ** (n * t)
    return '$' + str(p) + ' invested at ' + str(r) + '% for ' + str(t) + ' years compounded ' + str(n) + ' times per year is $' + str(int(A))


result = simple_interest_compound(int(input("What is the principal amount? ")),
                                  float(input("What is the rate? ")),
                                  int(input("What is the number of years? ")),
                                  int(input("What is the number of times the interest is compounded per year? ")))
print(result)

