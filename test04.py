"""
===============
Fool's Day 2014
===============

Today I wanted to create new task and found it is April 1 2014 - the Fool's Day when people are trying
to overjoke each other.

So here is a small programming problem without the problem statement. Nevertheless you can do it! Good
luck! :)

Example:

input data:
5
1 2
1 2 3
2 3 4
2 4 6 8 10
7 11 19

answer:
5 14 29 220 531
"""
print('')


def fool_day():
    dado, dados, trabalho, m, soma, somas = '', [], [], 0, 0, []
    with open('fool_day.txt') as arquivo:
        lista = list(arquivo)
    for k in range(0, len(lista)):
        dado += lista[k]
        dado = dado.replace('\n', '')
        dado = dado.split(' ')
        while m < len(dado):
            dados.append(int(dado[m]))
            m += 1
        trabalho.append(dados)
        dado = ''
        m = 0
        dados = []
    for k in range(0, len(trabalho)):
        while m < len(trabalho[k]):
            trabalho[k][m] *= trabalho[k][m]
            soma += trabalho[k][m]
            m += 1
        somas.append(soma)
        m = 0
        soma = 0
    return f'{somas}'.replace('[', '').replace(']', '').replace(',', '')


print(fool_day())



