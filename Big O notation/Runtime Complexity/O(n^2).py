'''
O(n^2) 
this is one of inefficient code since this cosume resource exponentially.
this will take N*N operation to complete the task (for O(n^2)).
and no matter what the power of N is (n^3,n^4 ...)
we will still count these as O(N^2).
'''
def nested_num (num):
    for i in range(num): # N opeartion
        for j in range(num): #N opeartion
            print(i,j) #N * N = N^2 opearion

print(nested_num(2))