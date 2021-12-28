
# Numpy Cheat Sheet

import numpy as np

np.linspace(0,2,9)                          # Add evenly spaced values btw interval to array of length
np.zeros((1,2))	                            # Create and array filled with zeros
np.ones((1,2))                              # Creates an array filled with ones
np.random.random((5,5))                     # Creates random array
np.empty((2,2))                             # Creates an empty array
x = np.arange(3)                            # Create an array with a range
arr = np.array([1, 3, 2, 4])                # Create array
arr = np.array([1, 2, 3, 4], ndmin = 2)     # Create array of 2 dimensions
print(arr.ndim)                             # Print array dimensions
print(arr[1, 0])                            # Slicing a two dimensional array
print(arr.dtype)                            # Print array data type
arr = np.array([1, 2, 3, 4], dtype='S')     # Specify data type
newarr = arr.astype('i')                    # Change data type
x = arr.copy()                              # Make a copy of the array
x = arr.view()                              # Make a view of the array
print(arr.shape)                            # Print array shape
newarr = arr.reshape(4, 3)                  # Reshape the array
arr = np.concatenate((arr1, arr2))          # Join two arrays 
np.vstack((a,b))                            # Stack array row-wise
np.hstack((a,b))                            # Stack array column wise
x = np.where(arr == 4)                      # Find all items equal to four
x = np.sort(arr)                            # Make a sorted array
np.append(a,b)                              # Append items to array
np.insert(array, 1, 2, axis)                # Insert items into array at axis 0 or 1
np.resize((2,4))                            # Resize array to shape(2,4)
np.delete(array,1,axis)                     # Deletes items from array
other = ndarray.flatten()                   # Flattens a 2d array to 1d
array = np.transpose(other)
array.T                                     # Transpose array
inverse = np.linalg.inv(matrix)             # Inverse of a given matrix
np.add(x,y)
x + y	                                    # Addition
np.substract(x,y)
x - y	                                    # Subtraction
np.divide(x,y)
x / y	                                    # Division
np.multiply(x,y)
x @ y	                                    # Multiplication
np.sqrt(x)                                  # Square Root
np.sin(x)                                   # Element-wise sine
np.cos(x)                                   # Element-wise cosine
np.log(x)                                   # Element-wise natural log
np.dot(x,y)                                 # Dot product
np.roots([1,0,-4])                          # Roots of a given polynomial coefficients
np.mean(array)                              # Mean
np.median(array)                            # Median
array.corrcoef()                            # Correlation Coefficient
np.std(array)                               # Standard Deviation
array.sum()                                 # Array-wise sum
array.min()                                 # Array-wise minimum value
array.max(axis=0)                           # Maximum value of specified axis	
array.cumsum(axis=0)                        # Cumulative sum of specified axis


# Data types
i = integer
b = boolean
u = unsigned_integer
f = float
c = complex_float
m = timedelta
M = datatime
O = object
S = string
