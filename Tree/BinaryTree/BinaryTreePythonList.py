'''
create
insert 
delete 
search
traverse
    -PreOrder:  root / Left / Right
    -InOrder:   Left / root / Right
    -PostOrder: Left / Right / root
    -LevelOrder: Level wiese
delete tree
'''
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

    def PostOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.PostOrderTraversal(index*2)
        self.PostOrderTraversal(index*2 +1)
        print(self.customList[index])

    def LevelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastUsedIndex ==0:
            return "Empty tree"
        else:
            for i in range(self.lastUsedIndex):
                if self.customList[i] == value:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex] = None
                    self.lastUsedIndex -=1
                    return "delete Successfully"
                

    def deleteTree(self):
        self.customList = None
        
newBT = BinaryTree(8)

newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert('Tea')
newBT.insert('Coffee')

# newBT.PreOrderTraversal(1)
# newBT.InOrderTraversal(1)
# newBT.PostOrderTraversal(1)

# newBT.deleteNode("Tea")
newBT.LevelOrderTraversal(1)