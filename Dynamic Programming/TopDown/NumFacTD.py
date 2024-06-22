def numberFactorTD(n, dp):
    if n in (0,1,2):
        return 1 # only one set of answer for N ==0 , 1 ,2
    elif n ==3:
        return 2 # {1,1,1} and {3}
    else:
        # generic formular for solving subproblem
        if n not in dp:
            subproblem1 = numberFactorTD(n-1, dp)
            subproblem2 = numberFactorTD(n-3, dp)
            subproblem3 = numberFactorTD(n-4, dp)
            dp[n] = subproblem1 + subproblem2 + subproblem3
        return dp[n]

print(numberFactorTD(5,{}))