'''

time_complexity =  O(n*m) --> N row * M Column operation required to go for all each data element
space complexity = O(1) --> just printing operation and comparing value
'''
import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
print('*----------------------------------------------------*')

def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'Value found at index '+ str(i) + " ," + str(j)
    return 'Value is not found'

print(searchTDArray(twoDArray,17))