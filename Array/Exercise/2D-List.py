'''

2D Lists
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
diagonal_sum(myList2D) # 15
'''

def diagonal_sum(lst):
    tmp = 0
    for i in range(len(lst)):
        tmp += lst[i][i]
    return tmp


myList2D= [[1,2,3],[4,5,6],[7,8,9]] 

 
print(diagonal_sum(myList2D)) # 15
