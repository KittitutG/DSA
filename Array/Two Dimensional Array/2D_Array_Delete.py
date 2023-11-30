'''
Deletion in NumPy will create new array excluding deleted row/column
hence we basically recreate another array which mean

time_complexity =  O(n*m) --> N row * M Column operation required to allocate each data elements
space complexity = O(1) --> N row * M Column operation required to allocate each data elements
'''
import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
print('*----------------------------------------------------*')

newTDArray = np.delete(twoDArray,0,axis=0)
print(newTDArray)