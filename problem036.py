from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of nested string.
    :return:
    """
    arq = open("problem036.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3, l4 = [], [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            for j in range(0, len(l1[i][k])):
                l2.append(int(l1[i][k][j]))
        l3.append(l2)
        l2 = []
    print(l3)
    return l3


def codeGuesser(l3):
    """
    This function reads guesses given by a guesser (except the last) and prints
    out the secret number chosen by the person who know the secret. It is guaranteed
    that exactly one solution exists.
    :param l3:
    :return:
    """
    idx0_0, idx1_0, idx2_0 = [], [], []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            if l3[i][-1] == 0:
                idx0_0.append(l3[i][0])
                idx1_0.append(l3[i][1])
                idx2_0.append(l3[i][2])
                break

    print(idx0_0)
    print(idx1_0)
    print(idx2_0)


codeGuesser(stringToInteger())
