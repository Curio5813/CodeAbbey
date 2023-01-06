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
    a, c, m, xc, l4 = 445, 700001, 2097152, l3[0][1], []
    loops = sum(l3[1])
    for i in range(loops):
        # This is the formula of Linear Congruential Generator
        nex = (a * xc + c) % m
        # This updating the value of nex
        xc = nex
        l4.append(nex)
    return l4


def funnyWordsGenerator(l4, l3):
    """
    This function take the parameters give by the functions above
    and return the words you generated separated by space.
    :return:
    """
    print(l3)
    con = "bcdfghjklmnprstvwxz"
    vow = "aeiou"
    word, idx1, idx2, n, l5 = "", 0, 0, 0, []
    for i in range(0, len(l4), n):
        if i >= len(l4) - 1:
            break   
        idx1 = l4[i] % 19
        word += con[idx1]
        idx2 = l4[i + 1] % 5
        word += vow[idx2]
    return print(word)


funnyWordsGenerator(lCG(stringToInteger()), (stringToInteger()))
