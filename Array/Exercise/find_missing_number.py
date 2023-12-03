'''
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100.

Example

missing_number([1, 2, 3, 4, 6], 6) # 5
'''

def missing_number(arr,n):
    '''
    find different between given sequnetial and array
    different = sum_of_sequential - sum_of_array
    this is only limited to find one missing number on array
    '''
    total  = n *(n+1) //2   # find total sum of sequntial N number  (arithmenthic)
    sumArr = sum(arr) #find sum of given array
    missing_number = total -sumArr
    return missing_number

print(missing_number([1, 2, 3, 4, 6], 6))