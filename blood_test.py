
def Blood_Alcohol(A, W, G, H):
    assert G == 'M' or 'F'
    if G == 'M':
        BAC = (A * 5.14 /W * 0.73) - (0.015 * H)
    if G == 'F':
        BAC = (A * 5.14 /W * 0.66) - (0.015 * H)

    if BAC <= 0.08:
        output = 'It is legal for you to drive.'
    else:
        output = 'It is not legal for you to drive.'

    return f'Your BAC is {BAC}.\n{output}'



result = Blood_Alcohol(int(input('What is total alcohol consumed, in ounces (oz) ')),
                       int(input('What is your body weight in pounds ')),
                       str(input('What your gender, (M for male and F for female) ')),
                       int(input('How many hours since your last drink ')))


print(result)
    
