class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0
    
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def kruskal_mst(graph):
    vertices = [i for i in range(len(graph))]
    edges = []

    # Tworzenie listy krawędzi w postaci (waga, wierzchołek_1, wierzchołek_2)
    for v in vertices:
        for neighbor, weight in graph[v]:
            edges.append((weight, v, neighbor))
    
    # Sortowanie krawędzi w kolejności niemalejącej wag
    edges.sort()
    
    mst = []
    ds = DisjointSet(vertices)
    
    # Przechodzenie przez posortowane krawędzie i dodawanie ich do MST, jeżeli nie tworzą cyklu
    for edge in edges:
        weight, v1, v2 = edge
        if ds.find(v1) != ds.find(v2):
            ds.union(v1, v2)
            mst.append(edge)
    
    return mst


# Przykładowe użycie algorytmu Kruskala dla MST
graph =[
[(1, 5), (2, 1)],
[(0, 5), (2, 2), (3, 1)],
[(0, 1), (1, 2), (3, 4), (4, 8)],
[(1, 1), (2, 4), (4, 3)],
[(2, 8), (3, 3)]
]

mst = kruskal_mst(graph)
for edge in mst:
    weight, v1, v2 = edge
    print(f"{v1} -- {v2}: {weight}")