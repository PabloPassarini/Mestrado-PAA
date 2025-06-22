from time import time

def imprimir_tabuleiro(tabuleiro):
    """Função para imprimir o tabuleiro de Sudoku de forma legível."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(tabuleiro[i][j], end=" ")
        print()


def encontra_lacuna(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            if tabuleiro[linha][coluna] == 0: return linha, coluna
    return None

def valida(tab, num, pos):
    linha, coluna = pos
    for col in range(len(tab[0])):
        if tab[linha][col] == num and col != coluna: #Verifica se um numero já existe na mesma linha, o "col != coluna" é para Garantir que não estamos comparando a célula com ela mesma.
            return False
    
    for row in range(len(tab)):
        if tab[row][coluna] == num and row != linha:
            return False
        
    
    #Verificando o bloco 3x3
    aux_x = coluna//3
    aux_y = linha//3

    for row in range(aux_y*3, aux_y*3+3):
        for col in range(aux_x*3, aux_x*3+3):
            if tab[row][col] == num and (row, col) != pos: return False
    
    return True


def resolve_sudoku(tab):
    posicao = encontra_lacuna(tab)
    if not posicao:
        return True
    linha, coluna = posicao

    for valor in range(1, 10):
        if valida(tab, valor, posicao):
            tab[linha][coluna] = valor

            if resolve_sudoku(tab):
                return True
            print()
            imprimir_tabuleiro(tab)
            tab[linha][coluna] = 0
    
    return False

if __name__ == "__main__":
    tabuleiro_exemplo = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    tabuleiro_exemplo2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    tabuleiro_dificil = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
    tac = time()
    if resolve_sudoku(tabuleiro_exemplo2):
        print("\nSolução Encontrada:")
        imprimir_tabuleiro(tabuleiro_exemplo2)
        tic = time()
        print('Tempo exec.: {:.2f}'.format(tic-tac))