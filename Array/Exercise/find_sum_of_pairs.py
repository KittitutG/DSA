'''
Find sum of pairs whih equal to given number and these pairs should be distinct eg. (1,1) ,(2,2) is not allowed
return index of those pair
Example

find_sum_pairs([1, 2, 3, 1, 2, 3, 4, 5], 6) 
(6 1) 
(6 4)
(7 0)
(7 3)
'''

def find_sum_pairs(arr,n):
    for i in range(len(arr)):
        for j in range(i+1):    #for next element
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == n:
                print(i,j)
find_sum_pairs([1, 2, 3, 1, 2, 3, 4, 5], 6) 