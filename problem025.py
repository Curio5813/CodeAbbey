from csv import reader


def stringToInteger():
    """
    This function takes a .csv file and return a list of
    integer.
    :return:
    """
    arq = open("problem025.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    return l3


def linearCongruentialGenerator(l3):
    """
    This function generate a pseudo-random number by obey
    the follow rule:

            Xnext = (A * Xcur + C) % M

    and returns the n-th member.
    :param l3:
    :return:
    """
    nex, cont, l4, = 0, 0, []
    for i in range(0, len(l3)):
        a = l3[i][0]
        c = l3[i][1]
        m = l3[i][2]
        xc = l3[i][3]
        n = l3[i][4]
        while cont < n:
            nex = (a * xc + c) % m  # This is the formula of Linear Congruential Generator
            xc = nex  # This updating the value of nex
            cont += 1
        l4.append(nex)
        cont = 0
    return print(*l4)


linearCongruentialGenerator(stringToInteger())
