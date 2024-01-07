import sys
import os
sys.path.insert(0,os.path.abspath('../..'))

from Queue.QueueLinkedList import Queue

class BSTNode:
    '''
    Binary Tree with additional properties
    Left Child < root < Right Child
    '''
    def __init__(self,data):
        self.data = data
        self.LeftChild = None
        self.RightChild = None

def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.LeftChild is None:
            rootNode.LeftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.LeftChild,nodeValue)
    else:
        if rootNode.RightChild is None:
            rootNode.RightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.RightChild,nodeValue)
    return "Node is successfully inserted"

def PreOrderTraversal(rootNode):
    if not rootNode: #if rootNode is none, stop criterea for recursive
        return
    print(rootNode.data)
    PreOrderTraversal(rootNode.LeftChild)
    PreOrderTraversal(rootNode.RightChild)

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
            if root.value.LeftChild is not None:
                custQueue.enqueue(root.value.LeftChild)
            if root.value.RightChild is not None:
                custQueue.enqueue(root.value.RightChild)

def searchNode(rootNode,value):
    if rootNode.data == value:
        return "found"
    elif value < rootNode.data:
        if value == rootNode.LeftChild.data:
            return "found"
        else:
            searchNode(rootNode.LeftChild,value)
    elif value > rootNode.data:
        if value == rootNode.RightChild.data:
            return "found"
        else:
            searchNode(rootNode.RightChild,value)

def getMinNode(BST):
    tempNode = BST.data
    while tempNode.LeftChild is not None:
        tempNode = tempNode.LeftChild
    return tempNode

def deleteNode(rootNode,value):
    if rootNode == None:
        return
    
    #travel on left
    if value < rootNode.data:
        rootNode.LeftChild = deleteNode(rootNode.LeftChild,value)
    #travel on right 
    elif value> rootNode.data  :
        rootNode.RightChild = deleteNode(rootNode.RightChild,value)

    #case when deleted node has a child node
    #we need to replace deleted node with child node
    else:
        #only one child
        if rootNode.LeftChild is None:
            tempNode = rootNode.RightChild
            rootNode = None #delete parent
            return tempNode
        if rootNode.RightChild is None:
            tempNode = rootNode.LeftChild
            rootNode = None #delete parent
            return tempNode
        
        #have two children
        minNode = getMinNode(rootNode.RightChild)
        rootNode.data = minNode.data
        rootNode.RightChild = deleteNode(rootNode.RightChild,minNode.data)
    return rootNode

def deleteTree(rootNode):
    rootNode.data = None
    rootNode.LeftChild = None
    rootNode.RightChild = None
    

newBST =BSTNode(None) 
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,200)
insertNode(newBST,60)


deleteNode(newBST,200)

# print(newBST.data)
# print(newBST.LeftChild.data)
LevelOrderTraversal(newBST)

deleteTree(newBST)