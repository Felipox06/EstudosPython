import numpy as np #Importando numpy

#Configurando a matrix 3x3 vazia, os símbolos dos players e a váriavel do player_atual para 0(para a alternancia)
tabuleiro = np.full((3, 3), " ", dtype=str)
players = ["X", "O"]
player_atual = 0

#Formata o tabuleiro no terminal
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-'*5)

#Verifica as possibilidades de vitória no jogo da velha(horizontal, vertical e diagonal)
def verificar_vencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]
    
    
    for L in range(3):
        if tabuleiro[0][L] == tabuleiro[1][L] == tabuleiro[2][L] != " ":
            return tabuleiro[0][L]
        
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]
    
    if not np.any(tabuleiro == " "):
        return "Empate"
    return None


#Pede os inputs para a jogada e verifica se ela é possível, depois verifica se houve alguma vitória e então alterna o turno.
while True:
    imprimir_tabuleiro(tabuleiro)
    print(f"Turno do jogador {players[player_atual]}")
    
    while True:
        try:
            linha = int(input("Escolha a linha (0-2):"))
            coluna = int(input("Escolha a coluna(0-2):"))
            if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " ":
                break 
            else:
                print("Posição inválida ou ocupada")
        except ValueError:
            print("Digite números entre 0 e 2")
            
    tabuleiro[linha, coluna] = players[player_atual]
    
    resultado = verificar_vencedor(tabuleiro)
    if resultado:
        imprimir_tabuleiro(tabuleiro)
        if resultado == "Empate":
            print("Empate!")
        else:
            print(f"Jogador {resultado} venceu!")
        break

    player_atual = 1 - player_atual