import time
def Compare_num(f, s, t):
    if f >= s:
        n = f
        if f >= t:
            n = f
        else:
            n = t
    else:
        n = s
        if s >= t:
            n = s
        else:
            n = t

    return f'The largest number is {n}.'


result = Compare_num(int(input('Enter the first number: ')),
                     int(input('Enter the second number: ')),
                     int(input('Enter the third number: ')))

print(result)


time.sleep(3)
