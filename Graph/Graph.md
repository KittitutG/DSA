# Graph Types
1. Unweighted - undirected
2. Unweighted - directed
3. Positive - Weighted - undirected
4. Positive - Weighted - directed
5. Negative - Weighted - undirected
6. Negative - Weighted - directed


# Graph representation in course
{
    A:[B,C,D],
    B:[A,E],
    C:[A,D],
    D:[A,C,E],
    E:[B,D]
}

# BFS VS DFS
BFS : get the first neighbour then to next one like a Queue
DFS : get the last neighbour then go backtracking like a Stack
both have: TC (V + E), SC (V + E)

when to use
BFS: known target is as near as starting point
DFS: known target is as far as strating point

# Cycle Graph
This is kind of grahp which one node can cameback to itself through travelling to other node (eg. A --> B --> C --> A)
# Negative Cycle Graph
This is happening when sum of distance from cycle grap is negatives
# Bellman Ford Algorithm 
This algorothm is used to handle Negative Cycle graph.
this can detect negative cycle graph.
nomarlly, this algorithm will run (Vertex - 1) times.
but if we run the additional 1 time, and the distance of each node change.
this mean Negative cyclic graph is happening.
and hence that is the Single shortest path that can happen before we run into a loop on cycle(distance will alway change)
further disscussion: https://www.youtube.com/watch?v=lyw4FaxrwHg