import numpy as np

arr = np.array([1,2,3,4,5], dtype = 'S')
print(arr)
print(arr.dtype)

arr = np.array([1,2,3,4,5], dtype = 'U')
print(arr)
print(arr.dtype)

# Value Error
# arr = np.array(['a',2,3,4,5], dtype = 'i5')
# print(arr)
# print(arr.dtype)


#f4 denotes 32bit float,  f8 - 64 bit float etc. others like f5 are invalid
arr = np.array([1,2,3,4,5], dtype = 'f4')
print(arr)
print(arr.dtype)

#changing the datatype using astype
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

#Difference in copy and view
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
y = arr.view()
arr[0] = 42

print(arr)
print(y)

#base check whether arr owns the data or not if yes it return none else the org array
print(x.base)
print(y.base)

#Shape 
# each value in tuple tells the number of elements un that particular dimension
arr = np.array( [5, 6, 7, 8])
print(arr.shape)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#Reshape - changing dimension, or adding and removing elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#cannot reshape this way give -> ValueError
# newarr = arr.reshape(4)
# print(newarr)

#returns the view of arr
print(newarr.base)

#Unknown dimension - we can pass -1 (can not be passed to more than 1 dimension)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#Flattening of arr
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)