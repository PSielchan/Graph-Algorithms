import heapq

# O( ( E + V )logV )
def Dijkstra(G, s):
    distance = [ float('inf') for _ in range(len(G)) ]
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    distance[s] = 0
    PQ = [(0,s)]
    while PQ:
        current_distance, vertex = heapq.heappop(PQ)
        visited[vertex] = True
        if current_distance > distance[vertex]:
            continue

        for neighbour, weight in G[vertex]:
            dist = current_distance + weight

            if dist < distance[neighbour] and not visited[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                heapq.heappush(PQ, (dist, neighbour))

    print("distance from ", s, ": ")
    print(distance)
    print("parents: ")
    print(parent)
    

G=[ [(1,1), (2,1), (4,10)],
    [(2,2)],
    [(3,10)],
    [(4,1)],
    []]

start = 0

Dijkstra(G, start)