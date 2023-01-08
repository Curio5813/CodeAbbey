from csv import reader


def stringToInteger():
    """
    This function open a csv file and return a list of integer.
    :return:
    """
    arq = open("problem072.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l3, l2 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    return l3


def lCG(l3):
    """
    This function generate a pseudo-random number by obey
    the follow rule:

            Xnext = (A * Xcur + C) % M

    and returns the n-th member.
    :param l3:
    :return:
    """
    a, c, m, xc, n, cont, l4, l5 = 445, 700001, 2097152, l3[0][1], 0, 0, [], []
    for i in range(l3[0][0]):
        while cont < l3[1][n]:
            # This is the formula of Linear Congruential Generator
            nex = (a * xc + c) % m
            # This updating the value of nex
            xc = nex
            l4.append(nex)
            cont += 1
        l5.append(l4)
        l4 = []
        cont = 0
        n += 1
    return l5


def funnyWordsGenerator(l5, l3):
    """
    This function take the parameters give by the functions above
    and return the words you generated separated by space.
    :param l5:
    :param l3:
    :return:
    """
    con = "bcdfghjklmnprstvwxz"
    vow = "aeiou"
    word, idx1, idx2, k, l6 = "", 0, 0, 0, []
    for i in range(l3[0][0]):
        for k in range(0, len(l5[i]), 2):
            idx1 = l5[i][k] % 19
            word += con[idx1]
            if k >= len(l5[i]) - 1:
                break
            idx2 = l5[i][k + 1] % 5
            word += vow[idx2]
        l6.append(word)
        word = ""
    return print(*l6)


funnyWordsGenerator(lCG(stringToInteger()), stringToInteger())
