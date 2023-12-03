'''
Middle Function
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''

'''
sol1: del
'''

def middle (arr):
    arr.pop()
    arr.pop(0)
    return arr

myList = [1, 2, 3, 4]
print(middle(myList))  # [2,3]


'''
sol2: slicing
'''
def middle2(arr):
    return arr[1:-1]
myList = [1, 2, 3, 4]
print(middle2(myList))  # [2,3]

