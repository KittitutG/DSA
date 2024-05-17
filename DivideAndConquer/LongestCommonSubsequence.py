'''
given 2 strings, find longest common sub string

s1 = "elephant"
s2 = "eretpat"
output = 5
LCS = "eepat"

subproplem
option1 match: f(1) + f(2:7, 2,6)
option2 mismatch take next string on s1: f(0) + f(3:7 , 2:6)
option2 mismatch take next string on s2: f(0) + f(2:7 , 3:6)
max(ops1, ops2, ops3)
'''

def findLCS(s1, s2, index1, index2):
    # base case
    if index1 == len(s1) or index2 == len(s2):
        return 0
    
    #matching
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    
    #not match
    else:
        op1 = findLCS(s1, s2, index1, index2+1)
        op2 = findLCS(s1, s2, index1+1, index2)
        return max(op1, op2)
    
print(findLCS("elephant","eretpat",0,0))