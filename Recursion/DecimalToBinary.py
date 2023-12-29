def decToBin(n):
    '''
    f(x) = x mod 2 + 10(f(x//2))
    '''
    assert int(n) == n,'Input must be integer!'
    if n ==0:
        return 0
    else:
        return n%2 + 10* decToBin(int(n/2))
    
print(decToBin(-16))