import numpy as np


arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

'''
Filtering only the even elements
'''
arr = np.array([1,2,3,4,5,6,7,8,9,10])

filter_arr = []

for ele in arr:
    if ele%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
newarr = arr[filter_arr]
print(newarr)

filter_arr = arr%2 == 1
newarr = arr[filter_arr]
print(newarr)
