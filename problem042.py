"""
==================
Blackjack Counting
==================

The game of Blackjack has very simple rules: players should take cards one by one trying to collect more points
than opponents, but not exceeding 21 (refer Wikipedia for complete rules).

The deck contains all cards from 2 to 10 inclusive, which are counted according to their value, also Kings,
Queens and Jacks which cost 10 points each and also Aces, which could be counted as 1 or 11 points, whatever is
better.

Let us learn the programming of scoring algorithm for such game.

Input data will contain the number of test-cases in the first line.
Then test-cases will follow on separate lines. Each test-case consists of several cards expressed with symbols:

2, 3, 4, 5, 6, 7, 8, 9,
T, J, Q, K - for 10, Jack, Queen, King,
A - for Ace.

Answer should contain the number of points in each test-case, not exceeding 21 - or the word Bust if the total
is greater than 21 (i.e. player immediately loss).

Example:

input data:
4
A T
2 K 4
3 A Q 8
A 3 3 3 A

answer:
21 16 Bust 21
"""
print('')


def blackjack_counting():
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    texto, lista, lista1, n, cont, resultados = '', [], [], 0, 0, []
    with open('blackjack_counting.txt') as arquivo:
        dados = list(arquivo)
    for k in range(0, len(dados)):
        texto += dados[k]
        texto = texto.replace('\n', '')
        texto.split(' ')
        lista.append(texto)
        texto = ''
    for k in range(0, len(lista)):
        lista1.append(lista[k].split(' '))
    for k in range(0, len(lista1)):
        while n < len(lista1[k]):
            if lista1[k][n] in '23456789':
                lista1[k][n] = int(lista1[k][n])
            n += 1
        n = 0
    for k in range(0, len(lista1)):
        while n < len(lista1[k]):
            if lista1[k][n] == 'T' or lista1[k][n] == 'J' or lista1[k][n] == 'Q' or lista1[k][n] == 'K':
                cont += 10
            if lista1[k][n] == 2 or lista1[k][n] == 3 or lista1[k][n] == 4 or lista1[k][n] == 5 or lista1[k][n] == 6 \
                    or lista1[k][n] == 7 or lista1[k][n] == 8 or lista1[k][n] == 9:
                cont += lista1[k][n]
            n += 1
        if 'A' in lista[k] and cont <= 10  and lista[k].count('A') == 1:
            cont += 11
        elif 'A' in lista[k] and cont <= 10 and lista[k].count('A') > 1:
            a = lista[k].count('A')
            cont += 11 + (a - 1)
        elif 'A' in lista[k] and cont > 10:
            a = lista[k].count('A')
            cont += a
        if cont <= 21:
            resultados.append(cont)
        if cont > 21:
            resultados.append('Bust')
        cont = 0
        n = 0
    return f'{[k for k in resultados]}'.replace('[', '').replace(']', '').replace(',', '').replace("'", '')


print(blackjack_counting())
