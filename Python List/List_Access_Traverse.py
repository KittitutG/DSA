#accessing data element
shoppingList =['Milk','Cheese','Butter']
print(shoppingList[0]) #access data at index N start from 0
print(shoppingList[-1]) #access data on reverse order start from -1

print('Hamburger' in shoppingList) #check if data is in list or not, return boolean


print('---------------------------------------------')
#traverse list
for i in shoppingList:
    print(i)