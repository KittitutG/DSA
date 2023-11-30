'''
Array is homogeneuos : only same data type is allow
Array is contagious: there's no gap between data element 
Array is unique by index

time_complexity = linear --> copy data from iterable object (list) to Array N times
space complexity = linear --> allocate N element to N slot on memory
'''


import array
'''
standard libreary for using array on python
'''
my_array = array.array('i')
print(my_array)
my_array1 = array.array('i',[1,2,3,4])
print(my_array1)

import numpy as np
'''
provide additional feature for array opeartion, need additional installation
'''
np_array = np.array([],dtype=int)
print(np_array)
np_array1 = np.array([1,2,3,4])
print(np_array1)