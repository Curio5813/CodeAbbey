from csv import reader
from statistics import mean


def stringToInteger():
    """
    This function convert strings to a integers and return a list.
    :return:
    """
    arq = open("problem016.csv")
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


def averageOfAnArray(l3):
    """
    This function receive a several arrays as argument and
    for each of which find an average value.
    :param l3:
    :return:
    """
    l4, l5 = [], []
    for i in range(0, len(l3)):
        l3[i].pop()
        l4.append(round(mean(l3[i])))
    return print(*l4)


averageOfAnArray(stringToInteger())
