'''
constarint
-array must be sorted

pros
-time performance will be better than linear search
'''

import math

def binary_search(array,value):
    start = 0 #left pointer
    end = len(array) - 1 #right pointer
    middle = math.floor((start+end)/2) #middle pointer

    while not(array[middle] == value) and start <= end: 
        if value < array[middle]:
            # if target is 12
            #  middle pointer(17) greater than target(12)
            # move end pointer to prior middle
            end = middle-1
        else:
            # if target is 20
            # middle pointer(17) lesser than target(20)
            # move start pointer to next middle
            start = middle +1
            
        # recalculate middle for each times until while condition met
        middle = math.floor((start+end)/2)


    if array[middle] == value:
        return middle
    else:
        return -1

myArray = [8,9,12,15,17,19,20,21,28]
print(binary_search(myArray,20))