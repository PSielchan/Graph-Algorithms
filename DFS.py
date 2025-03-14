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
            
    print("LIST")
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
DFS_list(G)