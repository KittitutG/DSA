'''
Element can be inserted at any given index.
this also mean time complexity could be vary

time_complexity = O(n) --> if we add at first index, we have to shift the rest to the rigt. hence this is linear
space complexity = O(1) --> we only assign value to new index
'''
import array


my_array1 = array.array('i',[1,2,3,4])
my_array1.insert(0,10)
print(my_array1)