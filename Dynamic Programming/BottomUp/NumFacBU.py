def NumFacBU(n):
    # base case
    dp = [1,1,1,2] # way to compose N by 1 , 3 , 4

    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-3] + dp[i-4]) # next element is construct by dp[n] = dp[i-1] + dp[i-3] + dp[i-4]

    return dp[n]

print(NumFacBU(5))
