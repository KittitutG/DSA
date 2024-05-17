'''
Given item that has weight and value.
find maximum value that can fit within limited weight.

eg. limit = 8
item: mango {value:3, profit:31}
apple {value:1, profit:26}
mango {value:2, profit:17}
mango {value:5, profit:72}

subproblem:
option1 = 31 + f(2,3,4)
option2 = 0 +f(2,3,4)
Max(option1 , option2)
'''


class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zoKnapsackProblem(item, capacity, currentIndex):
    if capacity <= 0 or currentIndex <0 or currentIndex >= len(item):
        return 0
    elif item[currentIndex].weight <= capacity:
        takeProfit = item[currentIndex].profit + zoKnapsackProblem(item,capacity- item[currentIndex].weight, currentIndex+1)
        skipProfit = zoKnapsackProblem(item, capacity, currentIndex+1)
        return max(takeProfit, skipProfit)
    else:
        return 0

mango = Item(31,3)    
apple = Item(26,1)    
orange = Item(17,2)    
banana = Item(72,5)
item_list = [mango, apple, orange, banana]

print(zoKnapsackProblem(item_list, 7 ,0))