from collections import deque

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
    

    def bfs(self,vertex):
        '''
        TC : O(V + E); V is vertex number, E is edege number --> only visit each vertex and edge once
        SC: O(V)
        '''
        visited = set() #result object
        visited.add(vertex)

        queue = deque([vertex]) #iterate object, using deque from collections lib for better performance
        while queue:
            current_vertex = queue.popleft() #popleft has better performace than pop(0)
            print(current_vertex)

            for adj_vertex  in self.adj_list[current_vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)

    def dfs(self,vertex):
        '''
        TC : O(V + E); V is vertex number, E is edege number --> only visit each vertex and edge once
        SC: O(V)
        '''
        visited = set() #result object
        stack = [vertex] #iterate object
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)

            for adj_vertex in self.adj_list[current_vertex]:
                if adj_vertex not in visited:
                    stack.append(adj_vertex)

        
my_graph = Graph()
my_graph.addVertex("A")
my_graph.addVertex("B")
my_graph.addVertex("C")
my_graph.addVertex("D")
my_graph.addVertex("E")

my_graph.addEdge("A","B")
my_graph.addEdge("A","C")
my_graph.addEdge("B","E")
my_graph.addEdge("C","D")
my_graph.addEdge("D","E")

my_graph.printGraph()

my_graph.dfs("A")







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

