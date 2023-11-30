'''
Insertion: data added must has the same dimension size as existing array

time_complexity =  O(n*m) --> N row * M Column operation required to shift data element
space complexity = O(n*m) --> N row * M Column operation required to shift data element on stack
'''
import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray,0,[[0,1,2,3]],axis= 1) #(array to insert, index, data element, axis: 0= row 1 = column)
print(newTwoDArray)

AppendTwoDArray = np.append(twoDArray,[[5],[6],[7],[8]],axis=1) #(array to insert, data element, axis: 0= row 1 = column)
print(AppendTwoDArray)