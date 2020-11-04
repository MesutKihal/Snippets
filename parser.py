import os
import re

def DataParser(data):
    data_array = []
    with open(data, "r") as f:
        content = f.readlines()
        for lines in content:
            x = re.split(',', lines)
            data_array.append(x)
        print('First Last Salary' + '\n' + '---------------')
        for items in data_array:
            print(*items)
    return

result = DataParser('Data File.txt')

print(result)
        
