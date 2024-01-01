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
        

# PreOrderTraversal(myTree)
# InOrderTraversal(myTree)
# PostOrderTraversal(myTree)
LevelTraversal(myTree)