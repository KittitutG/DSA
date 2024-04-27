class Item:
    def __init__(self,weight,value) :
        self.weight = weight
        self.value = value
        self.ratio = value / weight

    def __str__(self) -> str:
        return str(self.weight)

def KnapsackProblem(item, capacity):
    item.sort(key = lambda x: x.ratio, reverse =True)
    usedCapacity = 0
    totalValue = 0
    for i in item:
        if i.weight + usedCapacity <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value

        if usedCapacity == capacity:
            break
    print('Total value:' + str(totalValue))

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]
KnapsackProblem(cList,50)