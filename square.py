
def square_room(length,width):
    
    sf = length * width
    sm = sf * 0.09290304 
    return "\nYou entered dimensions of " + str(length) + " feet by "+ str(width) +" feet.""\nThe area is "+ str(sf) +" square feet" + "\n"+str(sm)+" square meters"

result = square_room(length = int(input('What is the length of the room in feet?')),
            width = int(input('What is the width of the room in feet?')))
print(result)





