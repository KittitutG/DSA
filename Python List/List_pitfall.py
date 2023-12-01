# some fundtion return NONE. this could lead to later downstream program
a = [1,2,3]
b = a.sort() #this return NONE object
print(b) # we cannot access sorted list with this variable since a.sort() return NONE, not sorted list

# too many choice can lead to mess up
b = [10]
print(a+b) #this is correct way to add element
a.append(b) #this is not 
print(a) #get a nested list, which can lead to false positive answer

# original list is lost
# due to some opeation will totally modify original list, keeping a copy to use in downstream is not bad idea
newList =[9,2,3,4,5]
print(newList)
newList.sort() #this will modify a list and cannot access the original
print(newList) 
print('-----------------')
# in order to access original list, we can keep a copy of them
newList =[9,2,3,4,5]
cloneList = newList[:]
newList.sort()
print(newList)
print(cloneList)
