'''
Array tranversal: we simply create loop to go to all element in array

time complexity: linear --> go throug each index
space complexity: constant --> only printing
'''


import array
my_array1 = array.array('i',[1,2,3,4])
print(my_array1)

def array_tranversal(array):
    for i in array:
        print(i)

array_tranversal(my_array1)