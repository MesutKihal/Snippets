def Readable_time(seconds):
    HH = 0
    MM = 0
    while seconds >= 3600:
        HH += 1
        seconds -= 3600
    while seconds >= 60:
        MM += 1
        seconds -= 60
    if HH < 10: HH = f'0{HH}'
    if MM < 10:MM = f'0{MM}'
    if seconds < 10: seconds = f'0{seconds}'
    return f'{HH} : {MM} : {seconds}'

result = Readable_time(int(input('>>> ')))
print(result)
