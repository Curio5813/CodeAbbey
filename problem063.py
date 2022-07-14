"""
=====================
Integer Factorization
=====================

Fundamental Theorem of Arithmetic states that any integer could be represented as product of one or more primes
and such representation is unique, for example:

1000 = 2 * 2 * 2 * 5 * 5 * 5
1001 = 7 * 11 * 13
1002 = 2 * 3 * 167
1003 = 17 * 59
1009 = 1009

Here we regard 1009 as a singular case of product of only one prime value - itself!

It is still unknown whether factorization could be done efficiently, i.e. fast enough for big numbers.
For example a number built as product of two 200-digit primes (i.e. having only 400 digits itself) will require
many thousand years to decompose it back into original pair of primes on modern computers.

Of course this precious fact has great significance in cryptography. If fast algorithm is ever found, many
crypting methods popular nowadays will become insecure at once! The classic example is an RSA algorithm of
which you can learn more from the dedicated exercise and other linked tasks.

Problem Statement
You will be given several numbers (not very large, so do not be afraid) to decompose them into products of primes.

Input data will contain amount of integers to factorize in the first line.
Next lines will contain one integer each (not exceeding 13 digits in length).
Answer should contain product representation for each of these integers, written like p1*p2*p3 where p1 ... p3
are some primes sorted in non-decreasing order. Products should be separated with spaces.

Example:

input data:
5
1000
1001
1002
1003
1009

answer:
2*2*2*5*5*5 7*11*13 2*3*167 17*59 1009
"""
print('')


def integer_factorization():
    dado, dados, n, fator, fatores = '', [], 2, [], []
    with open('integer_factorization.txt') as arquivo:
        lista = list(arquivo)
    for k in range(0, len(lista)):
        dado += lista[k]
        dado = dado.replace('\n', '')
        dados.append(int(dado))
        dado = ''
    for k in range(0, len(dados)):
        while dados[k] > 1:
            while dados[k] % n == 0:
                dados[k] /= n
                fator.append(n)
            else:
                n += 1
        n = 2
        fatores.append(fator)
        fator = []
    for k in range(0, len(fatores)):
        n = 0
        while n < len(fatores[k]):
            if n == len(fatores[k]) - 1:
                print(f'{fatores[k][n]}', end=' ')
                break
            print(f'{fatores[k][n]}*', end='')
            n += 1


integer_factorization()
