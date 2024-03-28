# Dijkstar can not handle Negative Cycle graph
# since we have a negative number on distance, 
# each time you try to cotinue the cycle. the distance will not be the same
# when distance is not the same. this is not single shortest path

import heapq

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
    
    def add_edge(self, weight, destination_node):
        edge = Edge(weight, self, destination_node)
        self.neighbour.append(edge)

class Dijkstar:
    def __init__(self) -> None:
        self.heap = []

    def calculate_distance(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            #pop out the element with lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                # this is use for skipper, some node can be update time over time.
                # since we use heapq, we will get the smallest distance
                # so we're safe to skip visited node
                continue
            #consider all neighbour
            for edge in actual_vertex.neighbour:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = edge.weigth + start.min_distance
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # push new node to heap collection to be calculate on next iteration
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True #this is to mark node as complete

    def get_the_shortest_path(self,vertex):
        print(f"The shortest path to the vertext is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name,end=" ")
            actual_vertex = actual_vertex.predecessor

# step1: create node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

#step2: add edege
nodeA.add_edge(6,nodeB)
nodeA.add_edge(10,nodeC)
nodeA.add_edge(9,nodeD)


nodeB.add_edge(16,nodeE)
nodeB.add_edge(13,nodeF)
nodeB.add_edge(15,nodeD)


nodeC.add_edge(6,nodeD)
nodeC.add_edge(5,nodeH)
nodeC.add_edge(21,nodeG)

nodeD.add_edge(8,nodeF)
nodeD.add_edge(7,nodeH)

nodeE.add_edge(10,nodeG)

nodeF.add_edge(4,nodeE)
nodeF.add_edge(12,nodeG)

nodeH.add_edge(2,nodeF)
nodeH.add_edge(14,nodeG)


algorithm = Dijkstar()
algorithm.calculate_distance(nodeA)
algorithm.get_the_shortest_path(nodeB)