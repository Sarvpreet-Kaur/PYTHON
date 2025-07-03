import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print("\n")
#Accessing elements 
print(arr[0])
print(arr[-1])

print(c[1, 2])
print(c[1][2])

print(d[1, 1, 1])

#Slicing arrays [Start : end] or [start: end: step] end is not included
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #slicing second row 1:4
print(arr[0:2, 2]) #slicing 3rd col 0:2

print(arr[0:2, 1:4])