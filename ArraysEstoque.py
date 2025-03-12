#Algoritmo de Busca Binária é o mais adequado

class Estoque:
    def __init__(self):
        """Inicializa o estoque com uma lista vazia de produtos."""
        self.produtos = []  # Lista de produtos ordenada por id_produto

    def adicionar_produto(self, nome, id_produto, preco, quantidade):
        """
        Adiciona um novo produto à lista de forma ordenada pelo id_produto.
        
        Args:
            nome (str): Nome do produto
            id_produto (int): ID único do produto
            preco (float): Preço do produto
            quantidade (int): Quantidade em estoque
        """
        produto = {"nome": nome, "id": id_produto, "preco": preco, "quantidade": quantidade}
        
        # Encontra a posição correta para inserir o produto
        pos = 0
        for p in self.produtos:
            if p["id"] < id_produto:
                pos += 1
            else:
                break
        
        # Verifica se o ID já existe
        if pos < len(self.produtos) and self.produtos[pos]["id"] == id_produto:
            print(f"Produto com ID {id_produto} já existe.")
            return
        
        # Insere o produto na posição correta
        self.produtos.insert(pos, produto)
        print(f"Produto {nome} adicionado com sucesso!")

    def buscar_produto(self, id_produto):
        """
        Busca um produto pelo id_produto usando busca binária.
        
        Args:
            id_produto (int): ID do produto a ser buscado
        
        Returns:
            dict or None: Dicionário do produto se encontrado, caso contrário None
        """
        inicio = 0
        fim = len(self.produtos) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.produtos[meio]["id"] == id_produto:
                return self.produtos[meio]
            elif self.produtos[meio]["id"] < id_produto:
                inicio = meio + 1
            else:
                fim = meio - 1
        return None

    def listar_produtos(self):
        """Lista todos os produtos no estoque."""
        for produto in self.produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")

# Teste do código
estoque = Estoque()
estoque.adicionar_produto("Caneta", 1, 2.50, 100)
estoque.adicionar_produto("Caderno", 2, 10.00, 50)
estoque.listar_produtos()

# Testando a busca
produto = estoque.buscar_produto(1)
if produto:
    print(f"Produto encontrado: {produto}")
else:
    print("Produto não encontrado")

produto = estoque.buscar_produto(3)
if produto:
    print(f"Produto encontrado: {produto}")
else:
    print("Produto não encontrado")