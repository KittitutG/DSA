# Topological sort
# this sort is operate by promising that
# "Any parent node will be done(sorted) before child node"

# Implementation: this sort is operate by using stack and recursive function altogether
# first we will go from starting point then recusively call child node till no child available
# then add that node to visited list and result stack, this will ensure that this node will not be added twice
# then we call back to parent node and add them to both visited/stack list untill every node is visited
# result will be kept in stack object in LIFO manner

from collections import defaultdict

class Graph:

    def __init__(self,numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def TopologicalSearchUtil(self, v , visited, stack):
        #add vertex to visit list
        visited.append(v)

        #iterate for each available child vertex
        for i in self.graph[v]:

            if i not in visited:
                #recursive call to next vertex
                self.TopologicalSearchUtil(i, visited, stack)
        
        #exit condition for recursive call
        #add vertex to stack list
        stack.insert(0, v)

    def TopologicalSort(self):
        visited = []
        stack = []

        #iterate for each available key in graph
        for i in list(self.graph):
            if i not in visited:
                self.TopologicalSearchUtil(i, visited,stack)
        print(stack)


customGraph = Graph(8)
customGraph.addEdge("A","C")
customGraph.addEdge("C","E")
customGraph.addEdge("E","H")
customGraph.addEdge("E","F")
customGraph.addEdge("F","G")
customGraph.addEdge("B","D")
customGraph.addEdge("B","C")
customGraph.addEdge("D","F")

customGraph.TopologicalSort()
