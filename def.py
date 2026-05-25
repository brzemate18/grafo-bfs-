from collections import deque
class BFS:
    @staticmethod
    def shortest_path(grafo, inicio, destino):
        if inicio == destino:
            return [inicio]
        fila = deque([(inicio, [inicio])])
        visitados = {inicio}
        while fila:
            vertice, caminho = fila.popleft()
            for vizinho in grafo.get(vertice, []):
                if vizinho not in visitados:
                    if vizinho == destino:
                        return caminho + [vizinho]
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))
        return None
if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    caminho = BFS.shortest_path(grafo, 'A', 'F')
    print(caminho)
    print(BFS.shortest_path(grafo, 'A', 'A'))
    print(BFS.shortest_path(grafo, 'A', 'E'))