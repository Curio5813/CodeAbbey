from csv import reader
from string import digits


def prime_chains():
    """

    :return:
    """
    arq = open("problem149.csv")
    l1 = reader(arq)
    l1 = list(l1)
    for i in range(0, len(l1)):
        for j in range(0, len(l1[i])):
            l1[i][j] = int(l1[i][j])
    print(l1)
    mod = 100000007
    inv_13 = 69230774
    for i in range(1, len(l1)):
        for j in range(0, len(l1[i])):
            hash_prime = 0
            digitos_reversos = []
            for _ in range(48):
                # Escolhemos um dígito 'D' aleatório ou fixo (ex: 1) para preencher
                # O dígito pode ser de 0 a 9 para formar um número normal
                D = 1

                # Descobrir qual tinha de ser o hash anterior para que,
                # com este 'D', o hash seguinte fosse o 'hash_alvo'
                hash_anterior = ((hash_prime - D) * inv_13) % mod

                # Guardamos o dígito que usámos
                digitos_reversos.append(str(D))
    print(*digitos_reversos)




prime_chains()