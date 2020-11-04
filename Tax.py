
def Tax_calc(amount, state):
    total = round(amount)
    if state == 'WI':
        total = amount + 0.55
        print('The subtotal is $', amount)

    return 'The total is $' + str(total)


result = Tax_calc(float(input('What is the order amount? ')) ,
                  str(input('What is the state? ')) ,)
print(result)        
    
