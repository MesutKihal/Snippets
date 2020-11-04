def Binary_loop(n):
    binary = ''
    t = 1024
    while 1 <= t:
        if n // t > 0:
            temp = t * (n // t)
            binary = binary + '1'
            n -= temp
        else:
            binary = binary + '0'
        t = t / 2

    return binary

result = Binary_loop(int(input('number >>> ')))

print(result)
