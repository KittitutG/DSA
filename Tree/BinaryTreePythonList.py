class BinaryTree:
    def __init__(self,size) -> None:
        self.customList = size *[None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insert(self,value):
        if self.lastUsedIndex +1 == self.maxSize:
            return "BT is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "Value is inserted succesfully"
    
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Hit"
        return "Miss"
    
    def PreOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.PreOrderTraversal(index*2) #left child
        self.PreOrderTraversal(index*2 + 1) #right child

    def InOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return 
        self.InOrderTraversal(index*2)
        print(self.customList[index])
        self.InOrderTraversal(index*2 +1)


newBT = BinaryTree(8)

newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert('Tea')
newBT.insert('Coffee')

# newBT.PreOrderTraversal(1)
newBT.InOrderTraversal(1)