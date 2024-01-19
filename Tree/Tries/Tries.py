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


    def searchString(self,word):
        cuurent = self.root
        for i in word:
            node = cuurent.children.get(i)
            if node == None:
                return False
            cuurent = node

        if cuurent.endOfString == True:
            return True #complete string
        else:
            return False #not a complete string


def deleteString(root,word,index):
    #delete would start to delte from leave up to common string
    ch = word[index]
    current = root.children.get(ch)
    deleteFlag = False
    
    if len(current.children) > 1: #move to next node
        deleteString(current,word,index+1)
        return False
    
    if index == len(word)-1: #last character of the word
        if len(current.children) >=1: #case when string is substring of others so will just set ending as True
            current.endOfString = False
            return False
        else: #delete node
            root.children.pop(ch)
            return True
        
    if current.endOfString == True:
        deleteString(current,word,index+1)
        return False
    
    deleteFlag = deleteString(current,word,index+1)
    if deleteFlag == True:
        root.children.pop(ch)
        return True
    else:
        return False


    

my_Trie= Trie()
my_Trie.insert("App")
my_Trie.insert("Apple")
deleteString(my_Trie.root, 'App', 0)
print(my_Trie.searchString('App'))