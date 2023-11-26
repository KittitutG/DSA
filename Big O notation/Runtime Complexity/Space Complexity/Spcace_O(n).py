'''
O(n)
this opeation will take N amount of memory.
operation will be stack each time they recursive themselve untill they found default case
'''
def sum(n):
    if n <=0:
        return 0
    return n + sum(n-1)

print(sum(3))