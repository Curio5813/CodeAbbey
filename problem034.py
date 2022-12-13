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
    li, ls, x = 0, 100, 50
    equation = l1[0] * x + l1[1] * sqrt(x ** 3) - l1[2] ** exp(-x / 50) - l1[3]
    print(equation)
    while equation != 0.000000:
        if equation < 0:
            li = x
            x = (ls + x) / 2
        elif equation > 0:
            ls = x
            x = (li + x) / 2
        equation = l1[0] * x + l1[1] * sqrt(x ** 3) - l1[2] ** exp(-x / 50) - l1[3]
        print(equation)
        print(x)
    print(x)


binarySearch(stringToFloat())
