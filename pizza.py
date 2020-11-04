def Pizza(people, pizza):
    assert people.isdigit() == True and pizza.isdigit() == True , 'Must be an integer'
    n = int(pizza) * 8
    pieces = n // int(people)
    left = n % int(people)
    return '\n' + str(people) + ' people with '+ str(pizza) +' pizzas' + '\nEach person gets ' + str(pieces) + ' pieces of pizza.' + '\nThere are ' + str(left) + ' leftover pieces.'


result = Pizza(input("How many people? "), input("How many pizzas do you have? "))
print(result)
