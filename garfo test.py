from collections import deque

class BFS:


    @staticmethod
    def traversal(grafo, inicio):

        visitados = set([inicio])
        fila = deque([inicio])
        ordem = []

        while fila:
            vertice = fila.popleft()
            ordem.append(vertice)

            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        return ordem

    @staticmethod
    def shortest_path(grafo, inicio, destino):

        if inicio == destino:
            return [inicio]

        fila = deque([(inicio, [inicio])])
        visitados = set([inicio])

        while fila:
            vertice, caminho = fila.popleft()

            for vizinho in grafo[vertice]:
                if vizinho == destino:
                    return caminho + [vizinho]

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))

        return None

    @staticmethod
    def distances(grafo, inicio):

        distancias = {inicio: 0}
        fila = deque([inicio])

        while fila:
            vertice = fila.popleft()

            for vizinho in grafo[vertice]:
                if vizinho not in distancias:
                    distancias[vizinho] = distancias[vertice] + 1
                    fila.append(vizinho)

        return distancias

    @staticmethod
    def connected_components(grafo):

        visitados = set()
        componentes = []

        for vertice in grafo:
            if vertice not in visitados:
                componente = []

                fila = deque([vertice])
                visitados.add(vertice)

                while fila:
                    v = fila.popleft()
                    componente.append(v)

                    for vizinho in grafo[v]:
                        if vizinho not in visitados:
                            visitados.add(vizinho)
                            fila.append(vizinho)

                componentes.append(componente)

        return componentes


class GridBFS:


    def __init__(self, grid):
        self.grid = grid
        self.linhas = len(grid)
        self.colunas = len(grid[0])
        self.direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4 direções

    def shortest_path(self, inicio, destino):

        fila = deque([(inicio, 0, [inicio])])
        visitados = {inicio}

        while fila:
            (lin, col), dist, caminho = fila.popleft()

            if (lin, col) == destino:
                return dist, caminho

            for dl, dc in self.direcoes:
                nova_lin, nova_col = lin + dl, col + dc
                nova_pos = (nova_lin, nova_col)

                if (0 <= nova_lin < self.linhas and
                        0 <= nova_col < self.colunas and
                        self.grid[nova_lin][nova_col] == 0 and
                        nova_pos not in visitados):
                    visitados.add(nova_pos)
                    fila.append((nova_pos, dist + 1, caminho + [nova_pos]))

        return -1, []

    def flood_fill(self, inicio):

        if self.grid[inicio[0]][inicio[1]] != 0:
            return []

        fila = deque([inicio])
        visitados = {inicio}
        area = []

        while fila:
            lin, col = fila.popleft()
            area.append((lin, col))

            for dl, dc in self.direcoes:
                nova_lin, nova_col = lin + dl, col + dc
                nova_pos = (nova_lin, nova_col)

                if (0 <= nova_lin < self.linhas and
                        0 <= nova_col < self.colunas and
                        self.grid[nova_lin][nova_col] == 0 and
                        nova_pos not in visitados):
                    visitados.add(nova_pos)
                    fila.append(nova_pos)

        return area




if __name__ == "__main__":

    print("=" * 50)
    print("EXEMPLO 1: GRAFO SIMPLES")
    print("=" * 50)

    grafo = {
        'A': ['D', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    bfs = BFS()

    print(f"Travessia BFS: {bfs.traversal(grafo, 'A')}")
    print(f"Caminho A->F: {bfs.shortest_path(grafo, 'A', 'F')}")
    print(f"Distâncias de A: {bfs.distances(grafo, 'A')}")
    print(f"Componentes: {bfs.connected_components(grafo)}")


    print("\n" + "=" * 50)
    print("EXEMPLO 2: LABIRINTO")
    print("=" * 50)

    labirinto = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    grid_bfs = GridBFS(labirinto)

    inicio = (0, 0)
    destino = (4, 4)

    dist, caminho = grid_bfs.shortest_path(inicio, destino)

    print(f"Distância: {dist}")
    print(f"Caminho: {caminho}")


    print("\nGrid com caminho (X = caminho, # = obstáculo, . = livre):")
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if (i, j) == inicio:
                print("S", end=" ")
            elif (i, j) == destino:
                print("D", end=" ")
            elif (i, j) in caminho:
                print("X", end=" ")
            elif labirinto[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


    print("\n" + "=" * 50)
    print("EXEMPLO 3: GRAFO DESCONEXO")
    print("=" * 50)

    grafo_desconexo = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A'],
        'D': ['E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': []
    }

    bfs2 = BFS()
    componentes = bfs2.connected_components(grafo_desconexo)

    print(f"Componentes conectados: {componentes}")
    for i, comp in enumerate(componentes):
        print(f"Componente {i + 1}: {comp}")


    print("\n" + "=" * 50)
    print("EXEMPLO 4: FLOOD FILL")
    print("=" * 50)

    imagem = [
        [0, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0]
    ]

    grid_bfs2 = GridBFS(imagem)
    area = grid_bfs2.flood_fill((0, 0))

    print(f"Área preenchida: {len(area)} pixels")
    print(f"Pixels: {area[:10]}...")

