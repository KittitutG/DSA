'''
Given 2D  Array, find min cost from (0,0) tp (N,M)
constraint: can only take either right or down direction

subproblem:
op1 = target_cell + left + N
op2 = target_cell + up + N
min (op1, op2)
'''

def findMinCost( twoDArray, row, col):
    if row == -1 or col ==-1:
        return float("inf")
    
    elif row ==0 and col ==0:
        return twoDArray[0][0]
    
    else:
        op1 = findMinCost( twoDArray, row-1, col)
        op2 = findMinCost( twoDArray, row, col-1)
        return twoDArray[row][col] + min(op1,op2)
    
TwoDList = [
            [4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3]
            ]

print(findMinCost(TwoDList,4,4))