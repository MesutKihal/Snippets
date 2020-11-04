
def Pass_valid(password):
    assert password != '', 'password <empty>'
    if password == '1324':
        answer = 'Welcome!'
    else:
        answer = 'I don\'t know you.'

    return answer


result = Pass_valid(str(input('What is the password? ')))

print(result)
