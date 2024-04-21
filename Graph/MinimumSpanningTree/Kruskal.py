import DisjointSet as dst

class Graph:
    def __init__(self, vertices) :
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = [] #Minimum Spanning Tree

    def add_edege(self, s , d, w):
        self.graph.append([s, d ,w])

    def add_node(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
            for s,d,w in self.MST:
                print("%s - %s: %s"%(s,d,w))

    def kruskal_algo(self):
        i, e = 0 , 0
        ds = dst.DisjointSet(self.nodes) 
        self.graph = sorted(self.graph, key=lambda item:item[2]) #reaarange and sorted by weigth in ascending order
        while e < self.V - 1: #while edges counter(e) not greater than vertices count
            s, d ,w =self.graph[i] #get graph detail
            i += 1 #move graph pointer
            x = ds.find(s)
            y= ds.find(d)
            if x != y:
                e+=1
                self.MST.append([s ,d ,w])
                ds.union(x,y)
        self.printSolution(s , d ,w)


g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")

g.add_edege("A", "B", 5)
g.add_edege("A", "C", 13)
g.add_edege("A", "E", 15)
g.add_edege("B", "A", 5)
g.add_edege("B", "C", 10)
g.add_edege("B", "D", 8)
g.add_edege("C", "A", 13)
g.add_edege("C", "B", 10)
g.add_edege("C", "E", 20)
g.add_edege("C", "D", 6)
g.add_edege("D", "B", 8)
g.add_edege("D", "C", 6)
g.add_edege("E", "A", 15)
g.add_edege("E", "C", 20)

g.kruskal_algo()