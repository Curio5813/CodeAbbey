"""
============
Prime Ranges
============

If you already solved Prime Numbers Generation - here is an inverse version of it.

Given several pairs of primes (like a, b) you are to tell for each of them the total quantity of primes in
the range limited by these values (inclusive), i.e. such p-s that:

isPrime(p) = true

    and

a <= p <= b

Input data: will contain the amount of pairs in the first line.
Next lines will contain one pair of primes each, the first value is always less than the second. All values
will be less than 3000000.

Answer should contain the quantity of primes in the ranges specified by these pairs.

Example:

input data:
3
5 19
11 29
2 23

answer:
6 6 9

Hint: you may start with generation of the array (or list) of primes in ascending order. However you will
need to use some effective method for searching values in this list, otherwise your program would work
significantly slower than it should.
"""
print('')


def prime_ranges():
    dado, dados, n, z, listas, numeros, tamanho_numeros = '', [], 0, 0, [], [], []
    with open('prime_ranges.txt') as arquivo:
        lista = list(arquivo)
    for k in range(0, len(lista)):
        dado += lista[k]
        dado = dado.replace('\n', '')
        dado.split(' ')
        dados.append(dado.split(' '))
        dado = ''
    lista = []
    for k in range(0, len(dados)):
        while n < len(dados[k]):
            lista.append(int(dados[k][n]))
            n += 1
        listas.append(lista)
        n = 0
        lista = []
    primos = []
    limite = 3000000 + 1
    nao_primo = set()
    for n in range(2, limite):
        if n in nao_primo:
            continue
        for f in range(n * 2, limite, n):
            nao_primo.add(f)
        primos.append(n)
    for k in range(0, len(listas)):
        while primos[z] < listas[k][0]:
            z += 1
        while listas[k][0] <= primos[z] <= listas[k][1]:
            numeros.append(primos[z])
            z += 1
        tamanho_numeros.append(len(numeros))
        z = 0
        numeros = []
    print(*tamanho_numeros)


prime_ranges()
