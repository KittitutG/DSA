def convertStringTD(s1, s2, index1, index2, dp):
 # base case when string length is different
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) -  index1
    # base case for moving  index to next char
    if s1[index1] == s2[index2]:
        return convertStringTD(s1, s2, index1+1 , index2+1,dp)

    #find min ops
    else:
        dictKey= str(index1) + str(index2)
        if dictKey not in dp:
            delOps = 1 + convertStringTD(s1 ,s2, index1, index2+1,dp)
            insOps = 1 + convertStringTD(s1 ,s2, index1+1, index2,dp)
            replaceOps = 1 + convertStringTD(s1 ,s2, index1+1, index2+1,dp)
            dp[dictKey] =  min(delOps, insOps, replaceOps)
        return dp[dictKey]
    
print(convertStringTD("table","tbrltt",0,0,{}))