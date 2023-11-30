'''
O(n)
this opeation will take only constant amount of memory.
below function is not stacking since they will simply call other function and do an opeation.
'''
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i,i+1)
    return total
    
def pair_sum(n,m):
    return n+m
print(pair_sum_sequence(4))