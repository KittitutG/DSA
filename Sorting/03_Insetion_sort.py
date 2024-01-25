'''
Insertion Sort
-Divide given array into two parts
-take 1st element from unsorted array and put it to correct position in sorted array
-repeat till unsorted array is empty

time complexity: O(N^2)
space complexity: O(1)

when to use:
    -insuffecient memory
    -easy to implement
    -got continuous inflow number and want to keep them
when to avoid
    -time complexity is really poor
'''

def insertion_sort(input_list):
    for i in range(1,len(input_list)):
        value = input_list[i]
        hole = i -1
        while hole >=0 and value < input_list[hole] :
            input_list[hole+1] = input_list[hole]
            hole -=1
        input_list[hole+1] = value
    print(input_list)

my_list = [5,10,9,6,7,2]
insertion_sort(my_list)