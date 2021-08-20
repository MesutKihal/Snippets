
i = 2
count = 0
while i < 1000000:
    if i == sum([int(digit)**5 for digit in str(i)]):
        count += i
    i += 1

print(count)
