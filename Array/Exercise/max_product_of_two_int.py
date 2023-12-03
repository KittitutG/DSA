'''
Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive.

Example

arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)
'''


'''
sol 1
'''
def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]
arr = [1, 7, 3, 4, 9, 5] 
print(max_product(arr)) # Output: 63 (9*7)


'''
sol2
'''
def max_product2(arr):
    max1 = 0
    max2 = 0
    total = 0
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i

    total = max1 * max2
    return total

arr = [2, 15, 3, 4, 7, 5] 

print(max_product(arr)) # Output: 105 (15*7)
           