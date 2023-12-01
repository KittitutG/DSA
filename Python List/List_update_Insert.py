myList = [1,2,3,4,5,6,7]
print(myList)

'''
update data element
'''
myList[2] = 33
print(myList)


'''
insert data element
'''
#1 insert() - at any given index
myList.insert(0,11)
print(myList)

#2 append() - at the end 
myList.append('newElement')
print(myList)

#3 extend() - add list to list
newList = ['Milk','Cheese','Butter']
myList.extend(newList)
print(myList)