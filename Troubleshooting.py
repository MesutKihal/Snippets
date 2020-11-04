answer = str(input('Is the car silent when you turn the key >>> '))
if answer == 'y':
    answer = str(input('Are the battery terminals corroded >>> '))
    if answer == 'y':
        answer = 'clean terminals and try starting again.'
    else:
        answer = 'replace cables and try again.'
else:
    answer = str(input('Does the car make a clicking noise >>> '))
    if answer == 'y':
        answer = 'Replace the battery.'
    else:
        answer = str(input('Does the car crank up but fail to start >>> '))
        if answer == 'y':
            answer = 'Check spark plug connections.'
        else:
            anwser = str(input('Does the engine start and then die >>> '))
            if answer == 'y':
                answer = str(input('Does your car have fuel injection >>> '))
                if answer == 'y':
                    answer = 'Get in for service.'
                else:
                    answer = 'Check to ensure the choke is opening and closing.'

print(answer)                    
                    
        
