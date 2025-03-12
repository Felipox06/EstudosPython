import networkx as nx

class RedeSocial:
    def __init__(self):
        self.grafo = nx.Graph()

    def adicionar_usuario(self, usuario):
        self.grafo.add_node(usuario)

    def adicionar_conexao(self, usuario1, usuario2):
        self.grafo.add_edge(usuario1, usuario2)

    def sugerir_amigos(self, usuario):
        amigos = set(self.grafo.neighbors(usuario))
        sugestoes = {}
        for amigo in amigos:
            for amigo_do_amigo in self.grafo.neighbors(amigo):
                if amigo_do_amigo != usuario and amigo_do_amigo not in amigos:
                    sugestoes[amigo_do_amigo] = sugestoes.get(amigo_do_amigo, 0) + 1
        return sorted(sugestoes, key=sugestoes.get, reverse=True)

# Teste
rede = RedeSocial()
rede.adicionar_usuario("Maria")
rede.adicionar_usuario("Bruno")
rede.adicionar_usuario("Carlos")
rede.adicionar_conexao("Maria", "Bruno")
rede.adicionar_conexao("Bruno", "Carlos")
print(f"Sugestões para Maria: {rede.sugerir_amigos('Maria')}")