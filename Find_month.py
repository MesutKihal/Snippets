months = {1: 'January', 2: 'February', 3:'March', 4:'April',
          5: 'May', 6: 'June', 7: 'July', 8:'August', 9:'September',
          10: 'October', 11: 'Novermber', 12: 'December',}

def Find_month(months, number):
    assert number.isdigit() == True, '<The number must be an integer>'
    return f'The name of the month is {months.get(int(number))}.'


result = Find_month(months, input('Please enter the number of the month: '))
print(result)
