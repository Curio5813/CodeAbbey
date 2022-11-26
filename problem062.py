from csv import reader


def stringToInteger():
    """
    This function open a csv file and return a list with integer.
    :return:
    """
    arq = open("problem062.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    print(l1)
    return l1


def primeNumbers():
    """
    This function return all prime numbers from 2 to
    3_000_000.
    :return:
    """
    p, n_p, lim = [], set(), 3_000_000
    for i in range(2, lim):
        if i in n_p:
            continue
        for k in range(i * 2, lim, i):
            n_p.add(k)
        p.append(i)
    return p


def primeRanges(l1, p):
    """
    This function take the parameter given by the functions above.
    One of a list o pair primes numbers and the second parameter is
    given a list of prime numbers until 3_000_000 and return the
    quantity of primes in the ranges specified by these pairs of
    prime numbers.
    :param l1
    :param p
    :return
    """
    idx0, idx1, l2, l3 = 0, 0, [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            # catching the index in the prime number's list.
            idx0 = p.index(l1[i][0])
            idx1 = p.index(l1[i][1])
        for m in range(idx0, idx1 + 1):
            l2.append(p[m])
        l3.append(len(l2))
        l2 = []
    return print(*l3)


primeRanges(stringToInteger(), primeNumbers())
