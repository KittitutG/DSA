def sumOfDigits(n):
    '''
    55 = 5+5 = 10
    f(x) = 55%10 + 55//10
    f(x) = x%10 + f(x//10)
    '''
    assert n >=0 and int(n) ==n, 'The number must be positive interger only!'
    if n ==0:
        return 0
    else:
        return int(n%10) + sumOfDigits(n//10)
    
print(sumOfDigits(94))