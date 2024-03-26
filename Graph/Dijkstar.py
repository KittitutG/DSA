#class edge 
class Edge:
    def __init__(self, weigth, start_vertex, target_vertex) :
        self.weigth = weigth
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


#class for node
class Node:
    def __init__(self, name):
        self.name = name

        #addittional properties for traversing
        self.visited = None
        self.predecessor = None #previous node
        self.neighbour = []
        self.min_distance = float("inf")

    #overide [Less Than] built in fuction
    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance