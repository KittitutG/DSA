myList = ['a','b','c','d','e','f']
#1. in opeartor --basically a linear search over the list
target = 'a'
if target in myList:
    print(f"{target} found")
else:
    print('not found')


print('------------------')
#2. Linear Search
def linear_search(p_list,target):
    for i,v in enumerate(p_list):
        if v == target:
            return i
    return -1

print(linear_search(myList,target))