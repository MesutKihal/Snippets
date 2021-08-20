
#Exercice 1
'''
f = lambda x:x+15
print(f(10))
'''
#Exercice 2
'''
import random

f = lambda x:x*(random.randint(1,5))
print(f(15))
'''
#Exercice 3
'''
tuple_1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
tuple_2 = sorted(tuple_1, key=lambda x:x[1])
print(tuple_2)
'''
#Exercice 4
'''
dict_1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dict_2 = sorted(dict_1, key=lambda x:x['color'])
print(dict_2)
'''
#Exercice 5
'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = list(filter(lambda x:x%2 == 0, list_1))
print(list_2)
'''
#Exercice 6
'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = list(map(lambda x:x**2, list_1))
print(list_2)
'''
#Exercice 7
'''
str_1 = 'wingardium leviosa'
f = lambda x:x[0] == 'w'
print(f(str_1))
'''
#Exercice 9
'''
int_1 = 5
f = lambda x:type(x) == int
print(f(int_1))
'''
#Exercice 10
'''
n = 5
f = lambda x:x.append((x[-1]+x[-2]))
l = [0, 1]
while len(l) < n:
    f(l)
print(l)
'''
#Exercice 11
'''
f = lambda x,a:a in x
print([n for n in [1, 2, 3, 5, 7, 8, 9, 10] if f([1, 2, 4, 8, 9], n)])
'''
#Exercice 12
'''
arr = [-1, 2, -3, 5, 7, 8, 9, -10]
new_arr = list(filter(lambda x:x>0, arr))
new_arr.extend(sorted(filter(lambda x:x<0, arr)))
print(new_arr)
'''
#Exercice 13
'''
arr = [1, 2, 3, 5, 7, 8, 9, 10]
even = len(list(filter(lambda x:x%2==0, arr)))
odd = len(list(filter(lambda x:x%2!=0, arr)))
print(even)
print(odd)
'''
#Exercice 14
'''
arr = ['Sunday', 'Monday', 'April', 'June', 'Weekend']
new_arr = list(filter(lambda x:len(x)==6, arr))
print(new_arr)
'''

