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
            actual_vertex = heapq.pop(self.heap)
            if actual_vertex.visited:
                # this is use for skipper, some node can be update time over time.
                # since we use heapq, we will get the smallest distance
                # so we're safe to skip visited node
                continue
            #consider all neighbour
            for edge in actual_vertex:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = edge.weight + start.min_distance
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
