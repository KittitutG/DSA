'''
Given two string, find minium operation to convert one to anothers
operation --> delete, insert , replace

eg.string1: table
1. string2:tgable -->delete --> comparing index: f(s1_index2, s2_index3)
2. string2:tble --> insert --> comparing index: f(s1_index3, s2_index2)
3. string2:trble --> replace --> comparing index: f(s1_index2, s2_index2)
'''

def findMinOperation(s1, s2, index1, index2):
    # base case when string length is different
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) -  index1
    # base case for moving  index to next char
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1 , index2+1)

    #find min ops
    else:
        delOps = 1 + findMinOperation(s1 ,s2, index1, index2+1)
        insOps = 1 + findMinOperation(s1 ,s2, index1+1, index2)
        replaceOps = 1 + findMinOperation(s1 ,s2, index1+1, index2+1)
        return min(delOps, insOps, replaceOps)

print(findMinOperation("table","tbrltt",0,0))