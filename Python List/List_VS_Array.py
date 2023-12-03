'''
1.Array is created with rich arithmethic operation
'''
import numpy as np
myArray = np.array([1,2,3,4],'i')
print(myArray)
print(myArray/2) 

myList = [1,2,3,4]
# print(myList/2) # this is not going to work

'''
2.List can be composed of mixed data type
'''
myArray = np.array([1,2,3,4,'j'],'i') #this is not allow and will throw an error
print(myArray)
print(myArray/2) 

myList = [1,2,3,4,'j']
print(myList)
