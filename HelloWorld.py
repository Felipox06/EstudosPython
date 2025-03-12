import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

caminho_principal = ["H", "E", "LL", "O", "WO", "RL", "D"]
G.add_nodes_from(caminho_principal)

for i in range(len(caminho_principal) - 1):
    G.add_edge(caminho_principal[i], caminho_principal[i+1], weight = 69)
    

nodes_extras = ["THEO", "DAVI"]
G.add_nodes_from(nodes_extras)

G.add_edge("H", "THEO", weight = 420)
G.add_edge("THEO", "D", weight = 420)
G.add_edge("H", "DAVI", weight = 420)
G.add_edge("DAVI", "D", weight = 420)

def find_shortest_path_dijkstra(graph, start, end):
    caminho = nx.dijkstra_path(graph, source = start, target = end, weight = "weight")
    return caminho

shortest_path = find_shortest_path_dijkstra(G, "H", "D")
print(shortest_path)

pos = {
    'H': (0, 0), 'E': (1, 0), 'LL': (2, 0), 'O': (3, 0),
    ' ': (4, 0), 'WO': (5, 0), 'RL': (6, 0), 'D': (7, 0),
    'THEO': (3.5, 1), 'DAVI': (3.5, -1)
}

edge_labels = nx.get_edge_attributes(G, "weight")

plt.figure(figsize=(12, 6))
nx.draw(G, pos, with_labels=True,
        node_size=800, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')
plt.title("Grafo Ponderado com Caminho Mais Curto (Dijkstra)")
plt.show()