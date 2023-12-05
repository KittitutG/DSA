'''
Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
'''

def check_same_frequency(list1,list2):
    if list1.sort() and list2.sort():
        return True
    return False
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))


'''
sol2: teacher sol
'''
def check_same_frequency2(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency2(list1, list2))
