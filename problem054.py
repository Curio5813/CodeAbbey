from csv import reader
from math import gcd


def stringToInteger():
    """
    This function open a .csv file and return a list of
    integer numbers.
    :return:
    """
    l2 = []
    arq = open("problem054.csv")
    l1 = reader(arq, delimiter="\n")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            num = int(l1[i][k])
            l2.append(num)
    print(l2)
    return l2


def pythagoreanTriples(l2):
    """
    This function takes the parameter given by the function above, a
    list of integers, which are the sum of the Pythagorean triples,
    and returns the number "a", the hypotenuse squared, that
    satisfies the equation a² = b² + c², of the Pythagoras Theorem.
    :param l2:
    :return:
    """
    l3, l4, i = [], [], 0
    for i in range(0, len(l2)):
        l4.append(0)
    for m in range(1, 10_000):
        for n in range(1, 10_000):
            if gcd(m, n) == 1 and m > n:
                # Euclid's formula to find the pythagorean triples.
                # m and n should to be prime each others.
                a = m ** 2 + n ** 2
                b = 2 * m * n
                c = (m ** 2 - n ** 2)
                l3.append(a)
                l3.append(b)
                l3.append(c)
                soma = sum(l3)
                if soma in l2:
                    idx = l2.index(soma)
                    h = a ** 2
                    l4.insert(idx, h)
                    l4.pop(idx + 1)
            l3 = []
    return print(*l4)


pythagoreanTriples(stringToInteger())
