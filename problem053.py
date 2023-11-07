import numpy as np
from csv import reader


def king_and_queen():
    """
    Programming of game playing algorithms, like Chess, have
    two principal tasks:

    assessing position, at least by checking which pieces could
    be taken;

    constructing a kind of minimax algorithm to select a move leading
    to position with best value. Let us start by solving a simple
    problem:

    There is a chessboard with 8 x 8 squares. There are the White King
    and Black Queen on it. Check whether the Queen could take the King.

    Remember - Queen could move to any distance vertically, horizontally
    or along any of two diagonals.

    Input data contain the number of test-cases in the first line.
    Next lines describe placement of the King and Queen for each testcase,
    by specifying their squares (King's first).
    Answer should give only letter 'Y 'or 'N' for each of test-cases, meaning that
    King could be taken or not respectively. Separate letters with spaces.
    :return:
    """
    arq = open("problem053.csv")
    dados = reader(arq, delimiter=" ")
    dados = list(dados)
    linhas = ['8', '7', '6', '5', '4', '3', '2', '1']
    colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pos, aux, positions, resposta, respostas, bol, cont1, cont2 = "", [], [], "", [], 0, 0, 0
    diagonais_acima_p, diagonais_abaixo_p, aux_acima_p, aux_abaixo_p = [], [], [], []
    diagonais_acima_sec, diagonais_abaixo_sec, aux_acima_sec, aux_abaixo_sec = [], [], [], []
    for i in range(0, len(linhas)):
        for k in range(0, len(colunas)):
            pos = colunas[k] + linhas[i]
            aux.append(pos)
        positions.append(aux)
        aux = []
    matriz = np.array(positions)
    diagonal_principal = [*matriz.diagonal(offset=0)]
    diagonais_acima = [matriz.diagonal(offset=i) for i in range(1, matriz.shape[0])]
    diagonais_abaixo = [matriz.diagonal(offset=-i) for i in range(1, matriz.shape[0])]
    diagonal_secundaria = [*np.diag(np.fliplr(matriz))]
    diagonais_acima_s = [np.diag(np.fliplr(matriz), k=i) for i in range(1, matriz.shape[0])]
    diagonais_abaixo_s = [np.diag(np.fliplr(matriz), k=-i) for i in range(1, matriz.shape[0])]
    for i in range(0, len(diagonais_acima)):
        for k in range(0, len(diagonais_acima[i])):
            aux_acima_p.append(diagonais_acima[i][k])
            aux_abaixo_p.append(diagonais_abaixo[i][k])
        diagonais_acima_p.append(aux_acima_p)
        diagonais_abaixo_p.append(aux_abaixo_p)
        aux_acima_p = []
        aux_abaixo_p = []
    for i in range(0, len(diagonais_acima_s)):
        for k in range(0, len(diagonais_acima_s[i])):
            aux_acima_sec.append(diagonais_acima_s[i][k])
            aux_abaixo_sec.append(diagonais_abaixo_s[i][k])
        diagonais_acima_sec.append(aux_acima_sec)
        diagonais_abaixo_sec.append(aux_abaixo_sec)
        aux_acima_sec = []
        aux_abaixo_sec = []
    for i in range(0, len(dados)):
        if dados[i][0][0] == dados[i][1][0]:
            resposta = "Y"
            respostas.append(resposta)
        elif dados[i][0][1] == dados[i][1][1]:
            resposta = "Y"
            respostas.append(resposta)
        elif dados[i][0] in diagonal_principal and dados[i][1] in diagonal_principal:
            resposta = "Y"
            respostas.append(resposta)
        elif dados[i][0] in diagonal_secundaria and dados[i][1] in diagonal_secundaria:
            resposta = "Y"
            respostas.append(resposta)
        else:
            for m in range(0, len(diagonais_acima_p)):
                if dados[i][0] in diagonais_abaixo_p[m] and dados[i][1] in diagonais_acima_p[m]:
                    resposta = "Y"
                    respostas.append(resposta)
                    break
                elif dados[i][0] in diagonais_abaixo_p[m] and dados[i][1] in diagonais_abaixo_p[m]:
                    resposta = "Y"
                    respostas.append(resposta)
                    break
                elif dados[i][0] in diagonais_acima_sec[m] and dados[i][1] in diagonais_acima_sec[m]:
                    resposta = "Y"
                    respostas.append(resposta)
                    break
                elif dados[i][0] in diagonais_abaixo_sec and dados[i][1] in diagonais_abaixo_sec[m]:
                    resposta = "Y"
                    respostas.append(resposta)
                    break
            else:
                resposta = "N"
                respostas.append(resposta)
    print(len(respostas))
    print(*respostas)


king_and_queen()
