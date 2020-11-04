
def bad_input(r):
    """ Handling bad inputs """
    if r.isdigit() == False:
        print('Sorry. That\'s not a valid input.')
        bad_input(input('What is the rate of return? '))
    else:
        yrs = 72 / int(r)
    return f'It will take {round(yrs)} years to double your initial investment.'


result = bad_input(input('What is the rate of return? '))
print(result)
