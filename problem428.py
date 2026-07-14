import string
from csv import reader


def broken_keyboard():
    """
    Paolo Durno descobre que seu teclado tem uma tecla B quebrado.
    Mas não é simplesmente "não digitar no char"! Além deste efeito
    óbvio,ele exclui misticamente algum dos caracteres anteriores:
    a letra maiúscula ou minúscula anterior mais próxima, dependendo
    se o botão foi pressionado Shift ou sem (ou seja, se B ou b deveria
    ser digitado).

    O objetivo é, pela string fornecida, produzir o resultado da digitação
    com este curioso teclado.

    Entrada fornece uma contagem de casos de teste a serem seguidos na primeira
    linha.
    As próximas linhas contêm um único caso de teste cada, em forma de strings,
    consistindo apenas de letras latinas.

    Resposta deve fornecer cordas malformadas resultantes, com espaço separado.
    :return:
    """
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    arq = open('problem428.csv')
    l1 = reader(arq)
    l1 = list(l1)
    n, ans = 0, []
    for i in range(0, len(l1)):
        for j in range(0, len(l1[i])):
            if i == 0 and j == 0:
                n = int(l1[0][0])
            else:
                break
        break
    cont, q = 0, 0
    for i in range(n):
        for j in range(1, len(l1)):
            if q == n:
                break
            l2 = l1[j][cont]
            if cont >= len(l2) - 1:
                cont = 0
                break
            for k in range(len(l2)):
                for l in l2:
                    if l == 'B':
                        if l2.find(l) == -1:
                            break
                        idx_l = l2.index(l)
                        for p in range(idx_l - 1, -1, -1):
                            if l2[p] in letras_maiusculas:
                                l2 = l2[:p] + l2[p + 1:]
                                break
                        l2 = l2.replace(l, '', 1)
                    if l == 'b':
                        if l2.find(l) == -1:
                            break
                        idx_l = l2.index(l)
                        for p in range(idx_l - 1, -1, -1):
                            if l2[p] in letras_minusculas:
                                l2 = l2[:p] + l2[p + 1:]
                                break
                        l2 = l2.replace(l, '', 1)
            print(l2)
            q += 1
        cont += 1


broken_keyboard()
