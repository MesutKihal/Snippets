import random
import string 

def Password_Generator(size):
    password = ''
    for _ in range(size):
        temp = random.choice(string.ascii_letters + string.digits + string.punctuation)
        password = password + str(temp)
    return password

result = Password_Generator(int(input('Enter the size  ')))

print(result)
