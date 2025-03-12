import heapq

class AgendadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        self.contador = 0

    def AddTarefa(self, tarefa, prioridade):
        heapq.heappush(self.tarefas, (-prioridade, self.contador, tarefa))
        self.contador += 1
        
    def executar_proxima(self):
        if self.tarefas:
            _, _, tarefa = heapq.heappop(self.tarefas)
            print(f"Executando: {tarefa}")
        else:
            print("Sem tarefas.")    
        
    def BuscarPrioridade(self):
        if self.tarefas:
            return self.tarefas[0][2]
        return None

agendador = AgendadorDeTarefas()
agendador.AddTarefa("Banal", 1)
agendador.AddTarefa("Normal", 5)
agendador.AddTarefa("Importante", 10)
print(f"Tarefa de maior prioridade: {agendador.BuscarPrioridade()}")  # "Tarefa Alta"