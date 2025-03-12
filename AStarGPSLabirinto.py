import heapq

def a_star_labirinto(grid, inicio, fim):
    def distancia_manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    linhas, colunas = len(grid), len(grid[0])
    direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direita, Baixo, Esquerda, Cima
    
    # Configuração de distâncias e caminho
    distancias = {inicio: 0}
    fila_prioridade = [(0 + distancia_manhattan(inicio, fim), inicio)]
    caminho = {inicio: None}
    
    while fila_prioridade:
        _, atual = heapq.heappop(fila_prioridade)
        if atual == fim:
            break
        for direcao in direcoes:
            vizinho = (atual[0] + direcao[0], atual[1] + direcao[1])
            if (0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas and 
                grid[vizinho[0]][vizinho[1]] == 0):
                nova_distancia = distancias[atual] + 1  # Custo de cada movimento é 1
                if vizinho not in distancias or nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    prioridade = nova_distancia + distancia_manhattan(vizinho, fim)
                    heapq.heappush(fila_prioridade, (prioridade, vizinho))
                    caminho[vizinho] = atual
    
    if fim not in caminho:
        return None
    rota = []
    no = fim
    while no is not None:
        rota.append(no)
        no = caminho[no]
    rota.reverse()
    return rota

# Labirinto 2D: 0 = caminho livre, 1 = parede
labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Teste: Encontrar caminho de (0,0) para (4,4)
inicio = (0, 0)
fim = (4, 4)
caminho = a_star_labirinto(labirinto, inicio, fim)
print("Caminho encontrado:", caminho)
# Saída esperada: [(0,0), (0,2), (0,3), (0,4), (1,4), (2,4), (3,4), (4,4)]