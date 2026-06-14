{
  "algoritmo": "BFS",
  "metodo": "shortest_path",
  "dados": {
    "grafo": {
      "A": ["B", "C"],
      "B": ["A", "D", "E"],
      "C": ["A", "F"],
      "D": ["B"],
      "E": ["B", "F"],
      "F": ["C", "E"]
    }
  },
  "parametros_execucao": {
    "inicio": "A",
    "destino": "F"
  },
  "resultado_esperado": [
    "A",
    "C",
    "F"
  ]
}
