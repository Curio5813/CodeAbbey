from csv import reader


def stringToInteger():
    """
    This function convert string for integer from a given.
    :return:
    """
    arq = open("problem018.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    return l1


def squareRoot(l1):
    """
    This function receive values X for which to perform calculations
    and number of steps N to perform. Use r = 1 at the beginning,
    and output resulting approximation (after N steps)to get approximately
    the square root of the numbers given, it's knew as Heron's Method.
    :return:
    """
    sqr, cont, l2 = 1, 0, []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            x = l1[i][0]
            n = l1[i][1]
            sqr, cont = 1, 0
            while cont < n:
                sqr = (sqr + (x / sqr)) / 2
                cont += 1
                sqr = sqr
        l2.append(sqr)

    return print(*l2)


squareRoot(stringToInteger())
