x = 0
y = 0
table = []

while x < 13:
    while y < 13:
        s = f'{x} X {y} = {x*y}'
        table.append(s)
        y += 1
    y = 0
    x +=1

for el in table:
    print(el)





    

    
            
        
            
        
