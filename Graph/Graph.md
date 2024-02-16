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