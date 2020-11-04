
def Filter_values(s):
    values = s.split()
    even = []
    for item in values:
        if int(item) % 2 == 0:
            even.append(str(item))
    return 'The even numbers are ' + ' '.join(even)


result = Filter_values(str(input('Enter a list of numbers, separated by spaces: ')))
print(result)
