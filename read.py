import os


def Write_Read():

    with open("Names.txt", "r") as f:
        contents = f.readlines()
        for lines in contents:
            print(lines)
        new_cnt = sorted(contents)
        
    with open("Names.txt", "w") as f:
        for lines in new_cnt:
            f.write(lines)
    print('\nTotal of 7 names','\n-----------------')
    with open("Names.txt", "r") as f:
        contents = f.readlines()
        for lines in contents:
            print(lines)
    return

ar = ['Ling, Mai',
      'Johnson, Jim',
      'Zarnecki, Sabrina',
      'Jones, Chris',
      'Jones, Aaron',
      'Swift, Geoffrey',
      'Xiong, Fong',]

f = open("Names.txt", "w+")

for el in ar:
    f.write(el)
    f.write('\n')
    
f.close()

result = Write_Read()

print(result)
    
