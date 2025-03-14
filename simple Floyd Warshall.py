def floyd_warshall(graph): #każdy z każdym
    n = len(graph)
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for u in range(len(graph)):
        for (v, weight) in graph[u]:
            dist[u][v] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

G = [ [ (1, 6), (2, 5), (3, 5) ],
  [ (4, -1) ],
  [ (1, -2), (4, 1) ],
  [ (2, -2), (5, -1) ],  
  [ (6, 3) ], 
  [ (6, 3) ],
  [] ]

T=floyd_warshall(G)
for i in range(len(T)):
    print(T[i])