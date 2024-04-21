This problem is to find path without having a starting point(source).
But rather, we goal toconnect all the dot together with minimum price.

# Disjoint set
Data Structure that keep track of set of element which are partitioned into a numbert of disjoint
and non overlapping sets and each sets have representative which helps in identifying that sets.

# Kruskal Algorithm
1.start with minimum distance from any node to any node
2.find next minimum
3.repeat step2 but min dist should not create any cycle.

# Prim Algorithm
1.Take one vertex as a starting point (as a 0). and others as infinity
2.for evry next vertices, if current weight is less than vertexs. update vertexs with weight
3.Mark as visited
4.Repeat for all the vertices