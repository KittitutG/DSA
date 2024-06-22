'''
DP: bottom up
divide problem into subploblem, find overlapping problem and start solving subproblem from start to result
'''

def fibTab(n):
    # static value on fib seq
    tb = [0, 1]

    # starting on index 2 till target
    for i in range(2, n+1):
        # find next element and store to table
        tb.append(tb[i-1] + tb[i-2])

    return tb[n-1]

print(fibTab(6))
    