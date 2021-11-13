


i = 2
previous = [0,1]
while True:
    temp = previous[0]+previous[1]
    previous[0] = previous[1]
    previous[1] = temp
    if len(str(previous[1])) == 1000:
        break
    i += 1
print(i)
