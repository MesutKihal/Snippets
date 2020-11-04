import random


questions = {'Is earth flat': 'No',
             'Are you a bitch': 'Yes',
             }

chosen = random.choice(list(questions.keys()))
print(chosen)
correct_ans = questions.get(chosen)
answer = input('what\'s your answer? ')

if answer == correct_ans:
    print('correct')
else:
    print('wrong')
