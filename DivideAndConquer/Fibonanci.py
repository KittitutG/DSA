def fib(n):
    if n <0:
        raise "N should never go below 0"
    elif n==1:
        return 0
    elif n==0:
        return 1
    return fib(n-1)+fib(n-2)

# fib(5): 0+1+1+2+3
print(fib(5))