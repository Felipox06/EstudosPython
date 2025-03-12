#Algoritmo de Busca Sequencial é o mais adequado

class Node:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None
        
class Playlist:
    def __init__(self):
        self.head = None
        self.atual = None
    
    def add_musica(self, musica):
        novo_node = Node(musica)
        if not self.head:
            self.head = novo_node
            self.atual = novo_node
        else:
            temp = self.head
            while temp.proximo:
                temp = temp.proximo
            temp.proximo = novo_node
            
    def remover_musica(self, musica):
        if not self.head:
            return
        if self.head.musica == musica:
            self.head = self.head.proximo
            if self.atual.musica == musica:
                self.atual = self.head
            return
        temp = self.head
        while temp.proximo:
           if temp.proximo.musica == musica:
               no_removido = temp.proximo
               temp.proximo = no_removido.proximo
               
               # Atualiza self.atual com segurança
               if self.atual.musica == musica:
                   self.atual = no_removido.proximo if no_removido.proximo else self.head
               return
           temp = temp.proximo
        print(f"Música '{musica}' não encontrada na playlist.")
    
    def tocar_proxima(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            print(f"Tocando: {self.atual.musica}")
        else:
            print("Fim da playlist.")

    def listar_musicas(self):
        if not self.head:
            print("Playlist vazia.")
            return
        temp = self.head
        while temp:
            print(temp.musica)
            temp = temp.proximo
            
    
    def BuscaSequencialMusica(self, musica_buscada):
        temp = self.head
        posicao = 0
        while temp:
            if temp.musica == musica_buscada:
                return posicao
            else:
                temp = temp.proximo
                posicao += 1
        return -1
    
    
    def musica_atual(self):  # Novo método
        if self.atual:
            print(f"Tocando agora: {self.atual.musica}")
        else:
            print("Nenhuma música está tocando.")


# Teste
playlist = Playlist()
playlist.add_musica("Música 1")
playlist.add_musica("Música 2")
playlist.add_musica("Música 3")
playlist.listar_musicas()
print(f"Posição de 'Música 2': {playlist.BuscaSequencialMusica('Música 2')}")
playlist.tocar_proxima()
playlist.remover_musica("Música 2")
playlist.musica_atual()
playlist.tocar_proxima()