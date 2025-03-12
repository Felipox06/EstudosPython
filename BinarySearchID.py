clientes = [
    {"id": 1, "nome": "Alice"},
    {"id": 2, "nome": "Bruno"},
    {"id": 3, "nome": "Carlos"},
    {"id": 4, "nome": "Daniela"},
    {"id": 5, "nome": "Eduardo"}
]

def Binary_Search(clientes, id_busca):
    inicio = 0
    fim = len(clientes) - 1
    while inicio <= fim:
        meio = (inicio+fim)//2
        if clientes[meio]["id"] == id_busca:
            return clientes[meio]
        elif clientes[meio]["id"] < id_busca:
            inicio = meio+1
        else:
            fim = meio-1
    return None

cliente = Binary_Search(clientes, int(input(f"Digite o ID que busca:")))
print(cliente if cliente else "Cliente não encontrado")