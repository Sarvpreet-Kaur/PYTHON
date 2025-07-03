import numpy as np

#Joining
''' we join 2 arrays using concatenate() function by axes. If axes
not specified default = 0
'''

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3 = np.concatenate((arr1,arr2))
print(arr3)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

arr = np.concatenate((arr1, arr2), axis=0)
print(arr)

'''
2.) Stacking - join along a new axis  
'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=0)
print(arr)


arr = np.hstack((arr1, arr2))
print(arr)

arr = np.vstack((arr1, arr2))
print(arr)


arr = np.dstack((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2, 3], [41, 51, 61]])
arr2 = np.array([[4, 5, 6], [4, 5, 6]])
arr = np.dstack((arr1, arr2), )
print(arr)

## Splitting
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
#Returns a list of arrays
print(newarr)

#Adjusts accordingly
#split() function can not adjust
newarr = np.array_split(arr, 4)
print(newarr)
print(type(newarr))

'''
Can be accessed using indexing
'''

# 2D Split
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis = 1)
print(newarr)

newarr = np.hsplit(arr, 3)
print(newarr)

newarr = np.vsplit(arr, 3)
print(newarr)

#Works on arr of 3 or more dimensions
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[ [10, 11, 12], [13, 14, 15], [16, 17, 18]]])
newarr = np.dsplit(arr, 3)
print(newarr)

#Searching


arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

#Sorting
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))