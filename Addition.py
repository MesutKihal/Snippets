
def Addition(ar):
    return f'The total {sum(ar)}.'

ar = []
for _ in range(5):
    ar.append(int(input('Enter a number: ')))

result = Addition(ar)
print(result)


