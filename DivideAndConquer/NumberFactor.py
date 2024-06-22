'''
# Given N Number, find how many way we can get the answer of combination of 1,3,4
eg. NumberFactor(5)
f(4) + 1 = [{1,1,1,1} + {4} + {3,1} + {1,3}]+1 = {1,1,1,1,1} + {4,1} + {3,1,1} +{1,3,1} -->4
f(3) + 2 = [{3}]+1+1 = {1,1,3}  -->1
f(1) + 4 = [{1}]+4 = {1,4} -->1
anser = 6 ways
generic formular
f(N-[given number factor]) + remainning
'''

def NumberFactor(n):
    # base case
    if n in (0,1,2):
        return 1 # only one set of answer for N ==0 , 1 ,2
    elif n ==3:
        return 2 # {1,1,1} and {3}
    else:
        # generic formular for solving subproblem
        subproblem1 = NumberFactor(n-1)
        subproblem2 = NumberFactor(n-3)
        subproblem3 = NumberFactor(n-4)
        return subproblem1 + subproblem2 + subproblem3
    
print(NumberFactor(5))