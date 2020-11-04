def self_checkout(p1,q1,p2,q2,p3,q3):
    
    subtotal = (p1 * q1) + (p2 * q2) + (p3 * q3)
    tax = 0.055
    total = float(subtotal) + (subtotal * tax)

    return 'Subtotal: ' + '$' + str(subtotal) + '\nTax: ' + '$' + str(subtotal * tax) + '\nTotal: ' + '$' + str(total)


result = self_checkout(int(input('Enter the price of item 1:')) ,
                       int(input('Enter the quantity of item 1:')) ,
                       int(input('Enter the price of item 2:')) ,
                       int(input('Enter the quantity of item 2:')) ,
                       int(input('Enter the price of item 3:')) ,
                       int(input('Enter the quantity of item 3:')))

print(result)
                       
                       
                       
                       
