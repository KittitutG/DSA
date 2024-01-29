'''
split data into small chank of bucket then sort each bucket individally before merge them together

time complexity: O(N^2) (depend on what sort algo we're using)
space conplexity: O(N)

when to use:
    -input data is uniformly distributed
whent to avoid:
    -space is concern
'''

import math

def insertion_sort(input_list):
    for i in range(1,len(input_list)):
        value = input_list[i]
        hole = i -1
        while hole >=0 and value < input_list[hole] :
            input_list[hole+1] = input_list[hole]
            hole -=1
        input_list[hole+1] = value
    return input_list

def bucketSort(customList):
    numberofBucket = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(numberofBucket):
        arr.append([])
    for j in customList:
        indexB = math.ceil(j*numberofBucket/maxValue)
        arr[indexB-1].append(j)
    
    for i in range(numberofBucket):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(numberofBucket):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k+=1
    return customList

my_list = [5,10,9,6,7,2]
print(bucketSort(my_list))