resting  = int(input('Enter resting pulse: '))
age = int(input('Enter your age: '))

print(f'\nResting Pulse: {resting}    Age:{age}\n','\nIntensity  |  Rate','\n----------------------')
intense = 0.55
table = []

while intense <= 1:
    THR = (((220 - age) - resting) * intense) + resting
    table.append(f'{round(intense * 100)}%         |     {round(THR)} bmp')
    intense += 0.05


for elm in table:
    print(elm)



        
    
