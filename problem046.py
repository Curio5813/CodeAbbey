"""
===========
Tic-Tac-Toe
===========

At this time we are not programming computer opponent for the game of Crosses and Noughts, but an important part
for such an algorith - the checking function, which can tell whether the game is ended and won by one or another
side.

The game is played on the square field 3 x 3. Let us suppose that the cells are numerated in the following way:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Two players put their marks (X for first and O for second) in turns into any of free cells remaining. One who
completes the straight line of three marks (three X-s or three O-s) immediately wins. Lines could be filled either
in rows or columns or one of two diagonals (8 lines possible in total). For example suppose the following moves
were performed:

 X   O
-------
 7
     5
 4
     1
 9
     2
 8

Which leads to the following position:

 O | O |
---+---+---
 X | O |
---+---+---
 X | X | X

with first player (Crosses) winning by completing the third row.

Problem statement
You will be given the sequence of moves (supposing the first move is always done by X) - by the numbers of cells
where marks are placed - and your task is to determine, at which step the first line was completed (by any side).

Input data contain the number of test-cases in the first line.
Next lines have one test-case each - exactly 9 numbers, describing cells to which moves are performed in order.
Answer should contain the number of the move at which game is won by one of players (starting from 1) or 0 if
the game is drawn (no winner) after the last move.

Example:

input data:
3
7 5 4 1 9 2 8 3 6
5 1 3 7 6 4 2 9 8
5 1 2 8 6 4 7 3 9

answer:
7 6 0
"""
print('')


def tic_tac_toe():
    dados, n, lista, jogada, jogadas, jogador1, jogador2, res = '', 0, [], [], [], [], [], []
    with open('tic_tac_toe.txt') as arquivo:
        dado = list(arquivo)
    for k in range(0, len(dado)):
        dados += dado[k]
        dados = dados.replace('\n', '')
        lista.append(dados.split(' '))
        dados = ''
    for k in range(0, len(lista)):
        while n < len(lista[k]):
            lista[k][n] = int(lista[k][n])
            n += 1
        n = 0
    for k in range(0, len(lista)):
        while n < len(lista[k]):
            jogada.append(lista[k][n])
            n += 1
        jogadas.append(jogada)
        n = 0
        jogada = []
    for k in range(0, len(jogadas)):
        while n < len(jogadas[k]):
            jogador1.append(jogadas[k][n])
            if 1 in jogador1 and 2 in jogador1 and 3 in jogador1:
                res.append(n + 1)
                break
            elif 4 in jogador1 and 5 in jogador1 and 6 in jogador1:
                res.append(n + 1)
                break
            elif 7 in jogador1 and 8 in jogador1 and 9 in jogador1:
                res.append(n + 1)
                break
            elif 1 in jogador1 and 4 in jogador1 and 7 in jogador1:
                res.append(n + 1)
                break
            elif 2 in jogador1 and 5 in jogador1 and 8 in jogador1:
                res.append(n + 1)
                break
            elif 3 in jogador1 and 6 in jogador1 and 9 in jogador1:
                res.append(n + 1)
                break
            elif 1 in jogador1 and 5 in jogador1 and 9 in jogador1:
                res.append(n + 1)
                break
            elif 3 in jogador1 and 5 in jogador1 and 7 in jogador1:
                res.append(n + 1)
                break
            n += 1
            if n >= len(jogadas[k]):
                if len(jogador1) == 5 and len(jogador2) == 4:
                    res.append(0)
                break
            jogador2.append(jogadas[k][n])
            if 1 in jogador2 and 2 in jogador2 and 3 in jogador2:
                res.append(n + 1)
                break
            elif 4 in jogador2 and 5 in jogador2 and 6 in jogador2:
                res.append(n + 1)
                break
            elif 7 in jogador2 and 8 in jogador2 and 9 in jogador2:
                res.append(n + 1)
                break
            elif 1 in jogador2 and 4 in jogador2 and 7 in jogador2:
                res.append(n + 1)
                break
            elif 2 in jogador2 and 5 in jogador2 and 8 in jogador2:
                res.append(n + 1)
                break
            elif 3 in jogador2 and 6 in jogador2 and 9 in jogador2:
                res.append(n + 1)
                break
            elif 1 in jogador2 and 5 in jogador2 and 9 in jogador2:
                res.append(n + 1)
                break
            elif 3 in jogador2 and 5 in jogador2 and 7 in jogador2:
                res.append(n + 1)
                break
            n += 1
        n = 0
        jogador1 = []
        jogador2 = []
    return f'{res}'.replace('[', '').replace(']', '').replace(',', '')


print(tic_tac_toe())
