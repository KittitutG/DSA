def gcd(a,b):
    '''
    gcd(48,18) 
    sol: 48%18 --> 2 remainder 12
         18%12 --> 1 remainder 6
         12%6  --> 2 remainder 0 
    gcd(48,18) = 6
    '''
    assert int(a) == a and int(b) == b,'The numbers must be integer only!'
    if a<0:
        a = -1*a
    if b<0:
        b = -1*b
    if b ==0:
        return a
    else:
        return gcd(b,a%b)
    
print(gcd(48,18))