'''
DP: Top down
divide problem into subploblem, find overlapping problem and store that overlapping problem that can be used later
'''

def fibMemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        # recursively call child element
        memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
    # return fib    
    return memo[n]

myDict = {}
print(fibMemo(6,myDict))