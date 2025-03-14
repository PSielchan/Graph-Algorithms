def find_eulerian_cycle(graph):
    # Sprawdź warunki dla cyklu Eulera
    for vertex in range(len(graph)):
        if len(graph[vertex]) % 2 != 0:
            return None  # Nie spełnia warunków

    start_vertex = 0  # Wybierz dowolny wierzchołek startowy
    eulerian_cycle = []  # Inicjalizacja cyklu Eulera

    def dfs(vertex):
        while graph[vertex]:  # Dopóki istnieją krawędzie wychodzące z wierzchołka
            next_vertex = graph[vertex].pop()  # Usuń krawędź z grafu
            for wektor in range(len(graph[next_vertex])):
                if graph[next_vertex][wektor]==vertex:
                    graph[next_vertex].pop(wektor)
                    break
            dfs(next_vertex)  # Rekurencyjnie przejdź do następnego wierzchołka
        eulerian_cycle.append(vertex)  # Dodaj wierzchołek do cyklu Eulera

    dfs(start_vertex)  # Rozpocznij od wierzchołka startowego

    eulerian_cycle.reverse()  # Odwróć cykl Eulera

    return eulerian_cycle

G = [[1, 2, 3, 4],
    [0, 2],
    [0, 1,3,3],
    [0, 4,2,2],
    [0, 3]]

print(find_eulerian_cycle(G))

