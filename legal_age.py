
def legal_age(age):
    if age >= 16:
        answer = 'You are old enough to legally drive.'
    else:
        answer = 'You are not old enough to legally drive.'

    return answer

result = legal_age(int(input('What is your age? ')))
print(result)
        
