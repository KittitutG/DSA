'''
find number of way to reach from start to target in 2D array with given cost
'''

def numberOfPaths(towDArray, row, col , cost):
    if cost < 0:
        return 0
    elif row ==0 and col == 0:
        if towDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row ==0:
        return numberOfPaths(towDArray, 0, col-1 ,cost - towDArray[row][col])
    elif col ==0:
        return numberOfPaths(towDArray, row-1, 0 ,cost - towDArray[row][col])
    else:
        op1 = numberOfPaths(towDArray, row-1, col ,cost - towDArray[row][col])
        op2 = numberOfPaths(towDArray, row, col-1 ,cost - towDArray[row][col])
        return op1 + op2
    
TowDArray = [
        [4,7,1,6],
        [5,7,3,9],
        [3,2,1,2],
        [7,1,6,3]
    ]
print(numberOfPaths(TowDArray,3,3,22))