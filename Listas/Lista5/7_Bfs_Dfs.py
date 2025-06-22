from collections import deque

def dfs(grafo, start, end):
    lista = [start]
    visitados = set()
    caminho = {}

    while lista:
        node = lista.pop()
        if node == end: break

        if node not in visitados:
            visitados.add(node)
            for vizinho in reversed(grafo[node]):
                if vizinho not in visitados:
                    caminho[vizinho] = node
                    lista.append(vizinho)

    return reconstruir_caminho(caminho, start, end)

def reconstruir_caminho(caminho_or, start, end):
    if end not in caminho_or: 
        return None
    path = [end]
    while path[-1] != start:
        path.append(caminho_or[path[-1]])
    path.reverse()
    return path

def bfs(grafo, start, end):
    queue = deque([start])
    visitados = set()
    caminho = {}

    while queue:
        node = queue.popleft()
        if node == end: break

        if node not in visitados:
            visitados.add(node)
            for vizinho in grafo[node]:
                if vizinho not in visitados and vizinho not in queue:
                    caminho[vizinho] = node
                    queue.append(vizinho)
    return reconstruir_caminho(caminho, start, end)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS path from A to F:", dfs(graph, 'A', 'F'))
print("BFS path from A to F:", bfs(graph, 'A', 'F'))
