import numpy as np


#   Creating a numpy Array
print('\tCreating Numpy Arrays\n-------------------------------------------\n')

a1 = np.array([5,4])        #|- 5 and 4 are elements of the array
a2 = np.arange(0,10,2)      #|- 0 is the fist element | 10 is the last element | 0 is the step
a3 = np.linspace(0,15,25)   #|- 0 is the start | 15 is the stop | 25 is the restep (50 is the default restep)
a4 = np.logspace(0,50,5)    #|- the start and end points are base**start and base**stop
a5 = np.zeros(10,int)       #|- it creates an array with 10 zeros, they are float by default
a6 = np.ones((2,4),int)     #|- the same thing for ones you can specify the N° of rows and columns
a7 = np.random.rand(2,3)    #|- An Array with random elements
a8 = np.full((2,3), 4)      #|- An Array of you choice

print('np.array([5,4])\n\n', a1)
print('\nnp.arange(0,10,2)\n\n', a2)
print('\nnp.linspace(0,15,25)\n\n', a3)
print('\nnp.logspace(0,50,5)\n\n', a4)
print('\nnp.zeros(10,int)\n\n', a5)
print('\nnp.ones((2,4),int)\n\n', a6)
print('\nnp.random.rand(2,2)\n\n', a7)
print('\nnp.full((3,2), 4)\n\n', a8)

#   NumPy most used functions
print('\n\tNumPy Array Functions\n-------------------------------------------\n')

s = np.shape(a1)
a1 = np.append(a1,-3)
a1 = np.insert(a1,1, 1)
mn = np.mean(a1)
md = np.median(a1)
std = np.std(a1)
ndim = np.ndim(a1)
dtype = a1.dtype
a1 = np.reshape(a1,(2,2))
a1 = np.flip(a1, 0)
a10 = np.concatenate((a7, a8), axis=0)

print('\nnp.std(a1)\n\n',std)
print('\nnp.shape(a1)\n\n',s)
print('\nnp.append(a1, 3)\n\n',a1)
print('\nnp.insert(a1, 1, 1)\n\n',a1)
print('\nnp.mean(a1)\n\n',mn)
print('\nnp.median(a1)\n\n',md)
print('\nnp.ndim(a1)\n\n',ndim)
print('\na1.dtype\n\n',dtype)
print('\nnp.reshape(a1, (2,2))\n\n', a1)
print('\nnp.flip(a1, 0)\n\n',  a1)
print('\nnp.concatenate((a7, a8), axis=0)\n\n', a10)

#   Slicing and subsetting
print('\n\tSlicing a Numpy Arrays\n---------------------------------------------\n')
a9 = np.array([[5,3,8,4,6],
               [2,1,9,7,0]])

print(a9[1,3])     #|- N°2 row, N°4 column                     >    7
print(a9[1,::2])   #|- N°2 row, all the columns  2 is the step >    [2,9,0]
print(a9[a9>2])    #|- get all elements bigger than 2          >    [5,3,8,4,6,9,7]
print(a9<6)        #|- returns an array of bool                >    [[False,True,False,True,False],[True,True,False,False,True]]
print(a9*3)        #|- multiply all elements with 3            >    [[15,9,24,12,18],[6,3,27,21,0]] 
