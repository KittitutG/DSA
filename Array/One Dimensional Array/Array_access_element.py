'''
time_complexity =  constant --> no iteration
space complexity = constant --> no stack need
'''

import array
my_array1 = array.array('i',[1,2,3,4])


def accessElement(array,index):
    if index >= len(array):
        print("out of bound index") #handling index that beyond array size
    else:
        print(array[index])

accessElement(my_array1,2)