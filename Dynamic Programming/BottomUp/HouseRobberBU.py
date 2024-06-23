def houseRobberBU(house):
    dp = [0]*(len(house)+2)
    for i in range(len(house)-1,-1,-1):
        dp[i] = max(house[i]+dp[i+2],dp[i+1])
    return dp[0]
house = [6,7,1,30,8,2,4]
print(houseRobberBU(house))    