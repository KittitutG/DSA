class TreeNode:
    def __init__(self,data,children = []):
        self.data = data
        self.children = children

    def __str__(self,level=0) -> str:
        ret = " "* level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks',[])

hot = TreeNode('Hot',[])
cold = TreeNode('Cold',[])

coffee = TreeNode('Coffee',[])
tea = TreeNode('Tea',[])

cola = TreeNode('Cola',[])
beer = TreeNode('Beer',[])

tree.addChild(hot)
tree.addChild(cold)

hot.addChild(coffee)
hot.addChild(tea)

cold.addChild(cola)
cold.addChild(beer)

print(tree)