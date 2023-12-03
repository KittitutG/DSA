'''
Check if given number is appear on array or not
return an index of element

List data type is not allow 
'''

import numpy as np

myAraay = np.array([1,2,3,0,4,6,7,8],'i')
def linear_search(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            print(i)
     
linear_search(myAraay,0)