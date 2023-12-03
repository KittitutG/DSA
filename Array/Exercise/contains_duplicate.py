'''
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
Hint: Use sets
'''

def contains_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
 
# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicates(nums))  # Output: True