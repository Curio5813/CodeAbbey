from csv import reader
from math import tan, radians


def stringToInteger():
    """
    This function open a .csv file and return a list with integer
    and float numbers.
    :return:
    """
    arq = open("problem172.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l1[i][k + 1] = float(l1[i][k + 1])
            l1[i][k + 2] = float(l1[i][k + 2])
            break
    return l1


def cloudAltitudeMeasurement(l1):
    """
    This function take a list given by the function above with integer
    and float numbers and calculate the clouds altitude return the
    several cloud's altitude calculated.
    :param l1:
    :return:
    """
    l2, h = [], 0
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            d1 = l1[i][0]
            a = radians(l1[i][1])
            b = radians(l1[i][2])
            h = (tan(a) * tan(b) * d1) / (tan(b) - tan(a))
            break
        l2.append(int(round(h, 0)))
    return print(*l2)


cloudAltitudeMeasurement(stringToInteger())
