import random

def winner(ar):
    return f'The winner is...{random.choice(ar)}' 


ar = []

for _ in range(20):
    n = str(input('Enter a name: '))
    if n == '':
        break
    else:
        ar.append(n)

result = winner(ar)
print(result)
