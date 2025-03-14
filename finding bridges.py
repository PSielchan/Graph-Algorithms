def find_bridges(graph):
    bridges = []
    n = len(graph)
    visited = [False] * n
    low = [float('inf')] * n
    parent = [-1] * n
    counter = 0

    def dfs(vertex):
        nonlocal counter
        visited[vertex] = True
        low[vertex] = counter
        counter += 1

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                parent[neighbor] = vertex
                dfs(neighbor)
                low[vertex] = min(low[vertex], low[neighbor])
                if low[neighbor] > low[vertex]:
                    bridges.append((vertex, neighbor))
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], low[neighbor])

    for v in range(n):
        if not visited[v]:
            dfs(v)

    return bridges

G=[ [1,5],
    [2,0],
    [3,1],
    [4,2],
    [5,3],
    [6,4,0],
    [5]]

print(find_bridges(G))