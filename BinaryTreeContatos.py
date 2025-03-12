#Por se basear em linkedlists, as Binary Trees também utilizam Nodes.
class Node:   
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.esquerda = None
        self.direita = None

class CatalogoContatos:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, telefone):
        self.raiz = self._inserir(self.raiz, nome, telefone)
    #A def _inserir chama a si própria, fazendo assim um metódo recursivo de loop implícito para percorrer a árvore.
    def _inserir(self, node, nome, telefone):
        if node is None:
            return Node(nome, telefone)
        if nome < node.nome:
            node.esquerda = self._inserir(node.esquerda, nome, telefone)
        else:
            node.direita = self._inserir(node.direita, nome, telefone)
        return node

    def listar(self):
        self._listar(self.raiz)

    def _listar(self, node):
        if node:
            self._listar(node.esquerda)
            print(f"{node.nome}: {node.telefone}")
            self._listar(node.direita)

# Teste
catalogo = CatalogoContatos()
catalogo.inserir("Carlos", "1234-5678")
catalogo.inserir("Ana", "8765-4321")
catalogo.inserir("Bruno", "1111-2222")
catalogo.listar()