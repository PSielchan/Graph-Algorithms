from collections import defaultdict

def bfs(G, source, sink, parent):
    visited = [False] * len(G)
    queue = []
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if not visited[v[0]] and v[1] > 0:
                queue.append(v[0])
                visited[v[0]] = True
                parent[v[0]] = u
                if v[0] == sink:
                    return True

    return False

def DFS_list(G, s = 0):

    def DFS_list_util(G, visited, parent, time, u):
        nonlocal T
        time[u] = T
        T += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_list_util(G, visited, parent, time, v)

    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    T = 0

    DFS_list_util(G, visited, parent, time, s)

    for i in range(len(G)):
        if not visited[i]:
            DFS_list_util(G, visited, parent, time, i)

def ford_fulkerson(G, source, sink):
    parent = [-1] * len(G)
    max_flow = 0

    while bfs(G,source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            u = parent[s]
            for v in G[u]:
                if v[0] == s:
                    path_flow = min(path_flow, v[1])
                    break
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            for i in range(len(G[u])):
                if G[u][i][0] == v:
                    G[u][i] = (G[u][i][0], G[u][i][1] - path_flow)
                    break
            for i in range(len(G[v])):
                if G[v][i][0] == u:
                    G[v][i] = (G[v][i][0], G[v][i][1] + path_flow)
                    break
            v = parent[v]

    return max_flow


# Przykład
g = [[(1, 10), (2, 10)],
     [(3, 4), (4, 8)],
     [(1, 2), (4, 5)],
     [(2, 9), (5, 10)],
     [(3, 6), (5, 10)],
     [(6, 10)],
     []]
source = 0
sink = 5
max_flow = ford_fulkerson(g, source, sink)

print("Maksymalny przepływ:", max_flow)
