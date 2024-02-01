from csv import reader
import gmpy2


def modular_exponentiation():
    """
    Now all you need to do is a calculation of raising A to power of B with
    result taken by modulo M.

    This operation is the cornerstone of many algorithms like generation of
    probable primes, generating keys for modern cryptography etc.

    Though some languages have built-in functions for such calculation, of
    course it would be better for you to find another approach!

    Input data will contain the number of testcases in the first line.
    Next lines will have three values for A B M each.
    Answer should give (A^B)%M for each case.
    :return:
    """
    arq = open("problem145.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    b, e, m, result = 0, 0, 0, []
    for i in range(0, len(l1)):
        potencia = gmpy2.powmod(int(l1[i][0]), int(l1[i][1]), int(l1[i][2]))
        result.append(potencia)
    print(*result)


modular_exponentiation()
