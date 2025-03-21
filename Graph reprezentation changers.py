def Matrix_to_list(G): # from matrix G to list of lists H
    H = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != float('inf'):
                H[i].append((j, G[i][j]))
    return H

def List_to_matrix(G, weighted = False, zeros = False): # from list of lists G to matrix H
    if zeros:
        H = [[0 for __ in range(len(G))] for _ in range(len(G))]
    else:
        H = [[float('inf') for _ in range(len(G))] for __ in range(len(G))]
    if not weighted:
        for v, edges in enumerate(G):
            for u in edges:
                H[v][u] = 1
    else:
        for v, edges in enumerate(G):
            for u, weight in edges:
                H[v][u] = weight
    

    return H

G = [[1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4, 5, 9],
    [3, 6],
    [3, 6],
    [4, 5, 7, 8],
    [6],
    [6, 9],
    [3, 8]]
print(List_to_matrix(G,False,True))