'''
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
'''
def first_second(lst):
    max1 =0
    max2 =0
    for i in lst:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and max1 != max2:
            max2 = i

    return max1,max2        


myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList)) # 90 87
