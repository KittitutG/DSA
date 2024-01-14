'''
create
insert -->level order traversal
delete -->get deepest node / delete / replace right child with deepest node
search
traverse
    -PreOrder:  root / Left / Right
    -InOrder:   Left / root / Right
    -PostOrder: Left / Right / root
    -LevelOrder: Level wiese
delete tree
'''
import sys
import os
sys.path.insert(0,os.path.abspath('..'))


from Queue.QueueLinkedList import Queue
class TreeNode:
    def __init__(self,data) :
        self.data = data
        self.leftChild = None
        self.rightChild = None



myTree = TreeNode('Drinks')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')

myTree.leftChild = leftChild
myTree.rightChild = rightChild

left2Child = TreeNode('Tree')
right2Child = TreeNode('Coffee')

leftChild.leftChild = left2Child
rightChild.rightChild = right2Child



'''
traversal leverage recursive fuction(memory stack)
'''
def PreOrderTraversal(rootNode):
    if not rootNode: #if rootNode is none, stop criterea for recursive
        return
    print(rootNode.data)
    PreOrderTraversal(rootNode.leftChild)
    PreOrderTraversal(rootNode.rightChild)
    
def InOrderTraversal(rootNode):
    if not rootNode: #if rootNode is none, stop criterea for recursive
        return
    InOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InOrderTraversal(rootNode.rightChild)

def PostOrderTraversal(rootNode):
    if not rootNode: #if rootNode is none, stop criterea for recursive
        return
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def LevelTraversal(rootNode):
    if not rootNode: #if rootNode is none, stop criterea for recursive
        return
    else:
        custQueue = Queue() #Helper class
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):     
            root = custQueue.dequeue()
            print(root.value.data)
            if  root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return "Tree is empty"
    else:
        tempQueue = Queue()
        tempQueue.enqueue(rootNode)
        while not (tempQueue.isEmpty()):
            root  = tempQueue.dequeue()
            if root.value.data == nodeValue:
                return "Hit"
            
            if  root.value.leftChild is not None:
                tempQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                tempQueue.enqueue(root.value.rightChild)
        return "Miss"
    
def InsertBT(rootNode,nodeValue):
    if not rootNode:
        rootNode = nodeValue
    else:
        tempQueue = Queue()
        tempQueue.enqueue(rootNode)
        while not (tempQueue.isEmpty()):
            root = tempQueue.dequeue()
            if root.value.leftChild is not None:
                tempQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = nodeValue
                return
            if root.value.rightChild is not None:
                tempQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = nodeValue    
                return
        
def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not custQueue.isEmpty():
            root = custQueue.dequeue()
            if  root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode
def deleteDeepNode(rootNode,dNode):
    if not rootNode:
        return 'Empty'
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not custQueue.isEmpty():
            root = custQueue.dequeue()
            if root.value == dNode:
                root.value = None
                return 'Hit'
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    custQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild =None
                    return
                else:
                    custQueue.enqueue(root.value.rightChild)

def deleteNode(rootNode,delNode):
    if not rootNode:
        return
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not custQueue.isEmpty():
            root = custQueue.dequeue()
            if root.value.data == delNode:
                deepestNode = getDeepestNode(rootNode)
                root.value.data = deepestNode.data
                deleteDeepNode(rootNode,deepestNode)
                return "delete succusfully"
            if  root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)      
        return "fail to delete"

def deleteTree(rootNode):
    rootNode.leftChild =None
    rootNode.rightChild =None
    rootNode.data = None

# PreOrderTraversal(myTree)
# InOrderTraversal(myTree)
# PostOrderTraversal(myTree)
# LevelTraversal(myTree)
# print(searchBT(myTree,'Cola'))
# newNode = TreeNode('Coffee')
# InsertBT(myTree,newNode)
# LevelTraversal(myTree)
# deleteNode(myTree,'Hot')
# LevelTraversal(myTree)
deleteTree(myTree)
LevelTraversal(myTree)
