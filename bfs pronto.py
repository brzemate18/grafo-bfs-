
from collections import deque


class BFS:
    @staticmethod
    def shortest_path(grafo, inicio, destino):
        fila = deque([inicio])
        visitados = {inicio}

        visited_order = []
        distances = {inicio: 0}
        predecessors = {inicio: None}

        while fila:
            vertice = fila.popleft()
            visited_order.append(vertice)

            if vertice == destino:
                path = []
                atual = destino
                while atual is not None:
                    path.append(atual)
                    atual = predecessors[atual]

                return {
                    "visited_order": visited_order,
                    "distances": distances,
                    "predecessors": predecessors,
                    "path": path[::-1],
                    "message": "Algoritmo executado com sucesso."
                }

            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    distances[vizinho] = distances[vertice] + 1
                    predecessors[vizinho] = vertice
                    fila.append(vizinho)

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

    resultado = BFS.shortest_path(grafo, 'A', 'F')
    print(BFS.shortest_path(grafo, 'A', 'F'))

