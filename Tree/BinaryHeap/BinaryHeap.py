'''
Binary heap is tree with additional properties
#1 parent mus be greater(MaxHeap)/lesser(MinHeap) or equal to children
#2 all level except the last one be completed (all filled excepted the last level)

MinHeap: parent is lesser or equal to child
MaxHeap: parent is greater or equal to child

Binary Heap --> find absolute(min/max) within O(logN) 
            --> insert new element within O(logN)

common ops
-create
-peek
-min/max
-traverse -->pre/in/post order, level order traversal
-size
-insert
-delete tree
'''

class Heap:
    def __init__(self,size):
        self.customList = (size+1) * [None] # +1 to reserver zero at beginning
        self.maxsize = size + 1 #boundary
        self.heapSize = 0 #node that being filled

def peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1] #get the 1st item in object

def siszeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize
    
def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode,index,heaptype):
    if not rootNode:
         return
    else:
        parent_index = int(index/2)
        if index <=1:
            return
        if heaptype == 'min':
            if rootNode.customList[index] < rootNode.customList[parent_index]:
                temp = rootNode.customList[parent_index]
                rootNode.customList[parent_index]  = rootNode.customList[index]
                rootNode.customList[index] = temp
            heapifyTreeInsert(rootNode,parent_index,heaptype)
        elif heaptype == 'max':
            if rootNode.customList[index] >  rootNode.customList[parent_index]:
                temp = rootNode.customList[parent_index]
                rootNode.customList[parent_index]  = rootNode.customList[index]
                rootNode.customList[index] = temp
            heapifyTreeInsert(rootNode,parent_index,heaptype)

def insertNode(rootNode,value,heaptype):
    if rootNode.heapSize + 1 == rootNode.maxsize:
        return "Tree is full, cannot inserted"
   
    rootNode.customList[rootNode.heapSize+1] = value
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heaptype)
    return "Inserted Successfully"

def heapifyTreeExtract(rootNode,index,heaptype):
    leftIndex = index * 2
    rightIndex = index * 2 +1
    swap = 0
    
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex: #one node

        if heaptype == 'min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp =rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return 
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp =rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heaptype == 'min':
            if rootNode.customList[leftIndex] <  rootNode.customList[rightIndex]:
                swap = leftIndex
            else:
                swap = rightIndex

            if rootNode.customList[index] > rootNode.customList[swap]:
                temp =rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swap]
                rootNode.customList[swap] = temp
           
        
        else:
            if rootNode.customList[leftIndex] >  rootNode.customList[rightIndex]:
                swap = leftIndex
            else:
                swap = rightIndex

            if rootNode.customList[index] < rootNode.customList[swap]:
                temp =rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swap]
                rootNode.customList[swap] = temp
    heapifyTreeExtract(rootNode,swap,heaptype)


def extract(rootNode,heaptype):
    if not rootNode:
        return
    else:
        extracted_node = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heaptype)   
        return extracted_node

def deleteTree(rootNode):
    rootNode.customList = None

my_heap = Heap(5)
insertNode(my_heap,4,'max')
insertNode(my_heap,5,'max')
insertNode(my_heap,2,'max')
insertNode(my_heap,1,'max')
extract(my_heap,'max')
LevelOrderTraversal(my_heap)
deleteTree(my_heap)