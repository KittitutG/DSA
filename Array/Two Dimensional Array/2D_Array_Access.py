'''
Insertion: data added must has the same dimension size as existing array

time_complexity =  O(1) --> Accessing data directky without looping
space complexity = O(n*m) --> No stack required for doing accessing or print
'''
import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

def accessElement (array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(colIndex[0]): #colIndex[0] will only focus column index
        print("out of bound")
    else:
        print(array[rowIndex][colIndex])

accessElement(twoDArray,1,3)
