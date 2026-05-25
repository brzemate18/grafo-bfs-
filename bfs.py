from collections import deque
class BFS:
    @staticmethod
    def shortest_path(grafo, inicio, destino):
        fila = deque([(inicio, [inicio])])
        visitados = {inicio}
        while fila:
            vertice, caminho = fila.popleft()
            if vertice == destino:
                return caminho
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
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