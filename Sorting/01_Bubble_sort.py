'''
repeatedly compare pair of items and swap them if they're in wrong order

time complexity: O(n^2)
space complexity: O(1)

when to use:
    -input is sorted 
    -space is a concern
    -easy to implement
when to avoid:
    -average time complexity is poor
'''

def bubbleSort(input_list):
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-i-1):
            if input_list[j+1] < input_list[j]:
                input_list[j],input_list[j+1] = input_list[j+1],input_list[j]
    print(input_list)

my_list = [5,10,9,6,7,2]
bubbleSort(my_list)