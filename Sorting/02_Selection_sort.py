''''
Selection sort
    -find min/max and swap them to the last index
    -inplace sort (no additional space require)

time complexity: O(N^2)
space complexity: O(1)

when to use:
    -insuffecient memory
    -easy to implement
when to avoid
    -time complexity is really poor
'''

def selection_sort(input_list):
    for i in range(len(input_list)):
        min_index = i
        for j in range(i+1,len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i],input_list[min_index] = input_list[min_index],input_list[i]
    print(input_list)

my_list = [5,10,9,6,7,2]
selection_sort(my_list)