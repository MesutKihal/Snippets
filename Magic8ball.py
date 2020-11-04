import random

def Magic8ball(Q, answers):
    answers = ["Yes", "No", "Maybe", "Ask again later."]
    return random.choice(answers)

result = Magic8ball(str(input('What\'s your question? ')),
                    answers = [])
print(result)
