import heapq

def dijkstra(grafo, inicio, fim):
    distancias = {local: float('inf') for local in grafo}
    distancias[inicio] = 0
    
    fila_prioridade = [(0, inicio)]
    
    caminho = {inicio: None}
    
    while fila_prioridade:
        distancia_atual, local_atual = heapq.heappop(fila_prioridade)
        if local_atual == fim:
            break
        if distancia_atual > distancias[local_atual]:
            continue
        
        for vizinho, distancia_km in grafo[local_atual].items():
            distancia = distancia_atual + distancia_km
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))
                caminho[vizinho] = local_atual  
    
    rota = []  
    local = fim
    while local is not None:
        rota.append(local)
        local = caminho.get(local)
    rota.reverse()
    if distancias[fim] != float('inf'):
        return rota, distancias[fim]
    else:
        return None, None  # Retorna dois valores

grafo_entrega = {
    'Depósito': {'Ponto A': 4, 'Ponto B': 10},
    'Ponto A': {'Depósito': 4, 'Ponto C': 8, 'Ponto D': 15},
    'Ponto B': {'Depósito': 10, 'Ponto D': 5},
    'Ponto C': {'Ponto A': 8, 'Ponto E': 7},
    'Ponto D': {'Ponto A': 15, 'Ponto B': 5, 'Ponto E': 12},
    'Ponto E': {'Ponto C': 7, 'Ponto D': 12}
}


rota, distanciaTotal = dijkstra(grafo_entrega, "Depósito", "Ponto E")
print("Rota encontrada:", rota,"\nDistância Total:", distanciaTotal)  