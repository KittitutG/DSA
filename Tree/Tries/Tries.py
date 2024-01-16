'''
Tries 
this is tree-based object that extend in heirachy order.
this often used with string.

Properties:
-one node can not have repetitive character
-one set should have end of string character

Application:
-spelling check
-autocorrect
'''

class TrieNode:
    '''
    even describes as a tree, implementation object would look more like map()
    which can describe as key:value
    '''
    def __init__(self):
        self.children = {}
        self.endOfString =False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word):
        '''
        case 1: balnk Trie
        case 2: string has prefix common in Trie
        case 3: string has common prefix that already complte in Trie
        case 4: string is exist in Trie
        '''
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)

            if  node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Cereated succssfully")


my_Trie= Trie()
my_Trie.insert("App")
my_Trie.insert("Apple")