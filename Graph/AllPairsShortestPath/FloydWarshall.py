'''
why Floyd Warshall
this algorithm best on this given situation
-the vertext is not reachable (no single edge related to vertice)
-two vertices are directly connected
    -this either be best solution(min distance) or we have options to improve
     by traveling through other node (less weight)
-two vertices are connected via other vertices (have multiple path to reach the same detination)

Negative cycle
-FW cannnot detect Negative Cycle
 since FW will ran into vertices once. so no loop(cycle) happening.
 hence cannot detact Negative Cycle
'''


INF = 9999

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF",end="   ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

def FloydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min( distance[i][j], distance[i][k] + distance[k][j] )

    printSolution(nV,distance)

G = [
    [0 , 8 , INF , 1],
    [INF , 0 , 1 , INF],
    [4 , INF , 0 , INF],
    [INF , 2 , 9 , 1]
]

FloydWarshall(4,G)