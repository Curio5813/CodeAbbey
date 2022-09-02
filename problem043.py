from csv import reader


def stringToFloat():
    """
    This function open a .csv file with list of strings and
    return a list of float.
    :return:
    """
    arq = open("problem043.csv")
    l1 = reader(arq, delimiter="\n")
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = float(l1[i][k])
            l2.append(l1[i][k])
    return l2


def diceRolling(l2):
    """
    This function receive a list of float as a parameter
    and return a list of integer from 1 to 6 by doing some
    steps described bellow to get this integers.
    :param l2:
    :return:
    """
    l3 = []
    for i in l2:
        i *= 6
        i = int(i)
        i = i + 1
        l3.append(i)
    return print(*l3)


diceRolling(stringToFloat())
