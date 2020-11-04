
def Temp_Convert(Choice):
    if Choice == 'C':
        tmp = 'Celsius' 
        temperature = int(input('\nPlease enter the temperature in Fahrenheit: '))
        output = (temperature - 32) * 5 / 9
    if Choice == 'F':
        tmp = 'Fahrenheit'
        temperature = int(input('\nPlease enter the temperature in Celsius: '))
        output = (temperature * 9 / 5) + 32

    return f'The temperature in {tmp} is {round(output)}.'


result = Temp_Convert(str(input('Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.\nYour choice: ')))

print(result)
