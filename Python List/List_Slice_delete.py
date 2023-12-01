'''
slicing
'''
myList = ['a','b','c','d','e','f']
myList[0:2] = ['x','y']
print(myList[:])


'''
delete
'''
#1 pop() - delete at given index, default with last index
myList.pop(1)
print(myList)

#2 del - delete data at given index
del myList[2]
print(myList)

#3 remove - remove data element from list
myList.remove('f')
print(myList)