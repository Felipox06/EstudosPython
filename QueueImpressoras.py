#FIFO (first in first out)

from collections import deque #deque(double ended queue) é eficiente na inserção e remoção em qualquer extremidade

class FilaImpressora:
    def __init__(self):
        self.fila = deque()

    def adicionar_documento(self, doc):
        self.fila.append(doc)
        print(f"Adicionado: '{doc}'")

    def imprimir(self):
        if self.fila:
            doc = self.fila.popleft()
            print(f"Imprimindo: '{doc}'")
        else:
            print("Fila vazia.")

    def ver_fila(self):
        print("Fila:", list(self.fila))

# Teste
impressora = FilaImpressora()
impressora.adicionar_documento("Doc1")
impressora.adicionar_documento("Doc2")
impressora.ver_fila()
impressora.imprimir()
impressora.ver_fila()