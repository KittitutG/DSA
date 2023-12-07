myTuple = ('a','b','c','d')
print('j' in myTuple) #find element, return boolean

print('----------------')
print(myTuple.index('b')) #find index of element, if found return index. else raise error

def searchTuple(tple,element):
    for i in range(len(tple)):
        if tple[i] == element:
            return f"The {element} found at {i} indexes"
    return "Element not found"
print(searchTuple(myTuple,'a'))