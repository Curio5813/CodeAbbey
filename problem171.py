from csv import reader
from math import tan, radians


def stringToInteger():
    """
    This function open a .csv file and return a list of integer.
    :return:
    """
    arq = open("problem171.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = float(l1[i][k])
    print(l1)
    return l1


def treeHeightMeasurement(l1):
    """
    This function take a parameter given by above function and return
    a list o integer that should contain the heights of the trees in
    the same order, rounded to the nearest integer.
    :param l1:
    :return:
    """
    h, l2 = 0, []
    for i in range(0, len(l1)):
        grd = l1[i][1] - 90
        d = l1[i][0]
        h = d * tan(radians(grd))
        h = round(h, 0)
        l2.append(int(h))
    return print(*l2)


treeHeightMeasurement(stringToInteger())
