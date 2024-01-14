'''
AVL
Binary search tree wuth additional properties
Tree must be balance, if not do a rotation
balance mean height of tree is not different more than 2 
rotation mena reassign node on that tree so tree would be balance

AVL is useful when we have imblance input (eg. sorted order dataset)
'''
import sys
import os
sys.path.insert(0,os.path.abspath('../..'))

from Queue.QueueLinkedList import Queue
class AVL:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not custQueue.isEmpty():
            root = custQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)

def searchNode(rootNode,value):
    if rootNode == None:
        return "Empty Tree"
    elif value < rootNode.data:
        if rootNode.leftChild.data == value:
            return "Found"
        else:
            searchNode(rootNode.leftChild,value)
    else:
        if rootNode.rightChild.data == value:
            return "Found"
        else:
            searchNode(rootNode.rightChild,value)



def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalanced(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode,value):
    '''
    Case 1: Rotation not required
    Case 2: Rotation required (imbalanced tree)
            **below condition is a path from disbalnced node to grandchild**
            --Lef Left condition -->right rotation
            --Lef Right condition -->left right rotation
            --Right Right condition--> left rotation
            --Right Left condition -->right left rotation

    '''

    '''
    pseudo code for Right rotation condition insert:
    rotateRight(disbalancedNode):
        newRoot = disbalancedNode.leftChild
        disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
        newRoot.rightChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
    '''

    '''
    pseudo code for Left rotation condition insert:
    rotateLeft(disbalancedNode):
        newRoot = disbalancedNode.rigthChild
        disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
        newRoot.leftChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
    '''

    if not rootNode:
        return AVL(value)
    elif value < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild,value)
    elif value > rootNode.data:
        rootNode.rightChild = insertNode(rootNode.rightChild,value)
    
    rootNode.height = 1 +max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))

    balance = getBalanced(rootNode)

    if balance > 1 and value < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and value > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and value < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    if balance < -1 and value > rootNode.rightChild.data:
        return leftRotate(rootNode)
    return rootNode

def getMinNode(rootNode):
    '''
    Helper function: this will be used when we removed root node.
    we require min value from  right subtree to replace the deleted node
    '''
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    else:
        return getMinNode(rootNode.leftChild)

def deleteNode(rootNode,value):
    '''
    Case 1: Rotation not required
    Case 2: Rotation required (imbalanced tree)
            **below condition is a path from disbalnced node to grandchild**
            --Lef Left condition -->right rotation
            --Lef Right condition -->left right rotation
            --Right Right condition--> left rotation
            --Right Left condition -->right left rotation

    '''
    if not rootNode:
        return
    elif value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        tempNode = getMinNode(rootNode)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,tempNode.data)
    rootNode.height = 1 +max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalanced(rootNode)
    if balance >1 and getBalanced(rootNode.leftChild) >=0:
        return rightRotate
    if balance >1 and getBalanced(rootNode.leftChild) <0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)        
        return rightRotate(rootNode)
    if balance <-1 and getBalanced(rootNode.rightChild) <=0:
        return leftRotate(rootNode)
    if balance <-1 and getBalanced(rootNode.rightChild) >0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode
    
def deleteTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    rootNode.height = 0

my_avl = AVL(5)
my_avl = insertNode(my_avl,10)
my_avl = insertNode(my_avl,15)
my_avl = insertNode(my_avl,20)
my_avl = deleteNode(my_avl,15)
deleteTree(my_avl)
LevelOrderTraversal(my_avl)