def factorial(n):
    '''
    n! = n*(n-1)*(n-2)*....*2*1
    n! = n*(n-1)!
    '''
    assert n >=0 and int(n) == n, 'The number must be positive integer only!!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
    
def fibonanci(n):
    '''
    sum of preceeding 2 value
    0,1,1,2,3,5
    5 = 3 + 2
    f(x) = f(x-1) + f(x-2)
    '''
    assert n >=0 and int(n) == n, 'The number must be positive integer only!!'
    if n in [0,1]:
        return n
    else:
        return fibonanci(n-1) + fibonanci(n-2)

    
print(factorial(-1))    