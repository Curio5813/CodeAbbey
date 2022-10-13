from csv import reader
from math import sqrt, exp


def stringToFloat():
    """
    This function open .csv values and return a list or float numbers.
    :return:
    """
    arq = open("problem034.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = float(l1[i])
    return l1


def binarySearch(l1):
    """
    This function take a list as parameter from the function above and
    calculate the Binary Search. It's the name of the simple and efficient
    algorithm for finding a position where Monotonic Function reaches
    the given value. Monotonic Function means that its values steadily grow
    with growing argument.

    Formula to Binary Search:

            A * x + B * sqrt(x ^ 3) - C * exp(-x / 50) - D = 0

    :param l1:
    :return:
    """
    print(l1)
    inf, sup, sx = 0, 100, 0
    for i in range(0, 100 + 1):
        while inf <= sup:
            h = (inf + sup) / 2
            if l1[0] * h + l1[1] * sqrt(h ** 3) - l1[2] ** exp(-i / 50) - l1[3] == 0:
                return print(h)
            if l1[0] * h + l1[1] * sqrt(h ** 3) - l1[2] ** exp(-i / 50) - l1[3] > 0:
                sup = h - 1
            else:
                inf = h + 1


binarySearch(stringToFloat())
