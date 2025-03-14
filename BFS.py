from collections import deque

def BFS(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        vertex = queue.popleft()
        for v in G[vertex]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                parent[v] = vertex
                time[v] = time[vertex] + 1

    print("time from ", s, ": ")
    print(time)
    print("parents: ")
    print(parent)

G=[ [1, 2, 8],
    [4, 5, 7],
    [9],
    [0, 10, 11],
    [13],
    [6, 7, 13],
    [],
    [8],
    [9],
    [],
    [9, 11],
    [],
    [0, 3],
    [12]]

BFS(G, 0)