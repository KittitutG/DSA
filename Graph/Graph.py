class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def addVertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adj_list.keys():
            print(vertex,": ",self.adj_list[vertex])

    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    

    def removeVertex(self,vertex):
        if vertex  in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

my_graph = Graph()
my_graph.addVertex("A")
my_graph.addVertex("B")
my_graph.addVertex("C")
my_graph.addVertex("D")

my_graph.addEdge("A","B")
my_graph.addEdge("A","C")
my_graph.addEdge("A","D")
my_graph.addEdge("B","C")
my_graph.addEdge("C","D")



my_graph.printGraph()

my_graph.removeVertex("D")
print("....")
my_graph.printGraph()








# class Graph:
#     def __init__(self,gdict =None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict

#     def addEdge(self,vertex,edge):
#         self.gdict[vertex].append(edge)


# my_dict = {
#     "a":["b","c"],
#     "b":["a","d","e"],
#     "c":["a","e"],
#     "d":["b","e","f"],
#     "e":["d","f","c"],
#     "f":["d","e"]
#             }


# graph = Graph(my_dict)
# graph.addEdge("e","g")
# print(graph.gdict['e'])

