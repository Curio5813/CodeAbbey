from csv import reader
from math import gcd, lcm


def stringToInteger(delimiter=None):
    """
    This function open a .csv file with a list of string and
    convert to a list of integer.r.
    :return:
    """
    arq = open("problem026.csv")
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


def greatestCommonDivisor(l3):
    """
    This function takes a list of integer from the function above
    and returns the Greatest Common Divisor and the Largest Common
    Multiple of that pairs of numbers.
    :param l3:
    :return:
    """
    div, lm, l4 = 0, 0, []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            div = gcd(l3[i][0], l3[i][1])
            lm = lcm(l3[i][0], l3[i][1])
        print(f"({div} {lm})", end=" ")


greatestCommonDivisor(stringToInteger())
