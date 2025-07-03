import numpy as np

#Iterating is done same as in lists using for each loop

#using nditer - eliminates the use of multiple for loops
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
    
#iterating with different data types
'''flags = ['buffered'] is used as numpy does not change the data type of element 
    in place so it require extra buffer space which is given by this 
    parameter
    If not used - gives TypeError
'''
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)


for x in np.nditer(arr, flags=['buffered'], op_dtypes=['U']):
    print(x)
    
#Iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    #1 3 5 7
    print(x)
    
    
    
#Enumerated Iterating using ndenumerate()

# 1D array
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

# 2D array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    # prints in tuple (x, y)
    print(idx, x)

