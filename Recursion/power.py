def power(base,exp):
    '''
    x^n = x*x*x*x*...x
    16 = 2*2*2*2
    16 = 2*2^(4-1)
    x^n = x*x^(n-1)
    '''
    assert int(exp) == exp ,'Exp number must be interger!'
    if exp ==0:
        return 1
    elif exp <0:
        return 1/base *power(base,exp+1)
    else:
        return base * power(base,exp-1)

print(power(2,-4))