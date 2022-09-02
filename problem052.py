from csv import reader
from math import hypot


def stringToInteger():
    """
    This function open a .csv file with a list of strings
    and return a list of integers.
    :return:
    """
    l2, l3 = [], []
    arq = open("problem052.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l2.sort()
        l3.append(l2)
        l2 = []
    return l3


def pythagoreanTheorem(l3):
    """
    This function receive as a parameters a list of integer
    and return letter "R" if a right, "A" acute or "O" obtuse
    triangle.
    :param l3:
    :return:
    """
    l4 = []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            h = hypot(l3[i][0], l3[i][1])
            if h > l3[i][2]:
                l4.append("A")
                break
            elif h < l3[i][2]:
                l4.append("O")
                break
            elif h == l3[i][2]:
                l4.append("R")
                break
    return print(*l4)


pythagoreanTheorem(stringToInteger())
