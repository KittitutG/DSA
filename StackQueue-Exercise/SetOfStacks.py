class PlateStacks():
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self) -> str:
        return self.stacks
    
    def push(self,value):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) ==0:
            self.stacks.pop()
        if len(self.stacks) ==0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self,stacknum):
        if len(self.stacks[stacknum]) > 0:
            return self.stacks[stacknum].pop()
        else:
            return None
        
cusStack = PlateStacks(2)

cusStack.push(5)
cusStack.push(6)

cusStack.push(3)
cusStack.push(7)

cusStack.push(9)
cusStack.push(10)


print(cusStack.pop_at(2))
print(cusStack.pop_at(1))
print(cusStack.pop_at(0))
