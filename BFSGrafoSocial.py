import networkx as nx
import matplotlib.pyplot as plt

# Criação do grafo
G = nx.Graph()
G.add_edges_from([("Maria", "Bruno"), ("Bruno", "Carlos"), ("Maria", "Daniela"), ("Daniela", "Eduardo")])

# Visualização
nx.draw(G, with_labels=True)
plt.show()


#Mesmo já sendo um método pronto do Networkx, programei manualmente para poder praticar e aprender a lógica
def bfs_caminho(grafo, inicio, fim):
    visitados = set()
    fila = [[inicio]]
    while fila:
        caminho = fila.pop(0)
        usuario = caminho[-1]
        if usuario not in visitados:
            vizinhos = grafo[usuario]
            for vizinho in vizinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                if vizinho == fim:
                    return novo_caminho
            visitados.add(usuario)
    return None

# Teste
caminho = bfs_caminho(G, "Maria", "Eduardo")
print("Caminho:", caminho)  # ['Ana', 'Daniela', 'Eduardo']