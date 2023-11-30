'''
Array is not allow empty space between element(contagious properties)
so deletion's time complxity will be vary
eg. [1,2,3,4,5]
1st scenario: delete 5 will only take O(1) since we can direcly remove the last element
2nd scenario: delete 3 will take O(n) since we not only remove 3 from array. but we also required to shift the rest of element to the left
[1,2,3,4,5]
    |
    |
[1,2,(),4,5] 
    |
    |
[1,2,4,5]   

time_complexity =  linear/Constant --> depent on scenrio. taking worst would be O(n)
space complexity = constant --> no stack need
'''

import array
my_array1 = array.array('i',[1,2,3,4])

my_array1.remove(3) #remove data element