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


my_avl = AVL(10)
