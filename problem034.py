from csv import reader
from math import sqrt, exp


"""
    Programming of Binary Search is the common task since it is used
    for searching through sorted arrays (that's why we learnt sorting)
    as well as for solving math equations. Let us practice the latter
    application. Please kindly refer to the Binary Search article for
    thorough explanations if you feel not well acquainted with the idea
    of the algorithm.

    The goal is to solve the equation which has the following form:


    A * x + B * sqrt(x ^ 3) - C * exp(-x / 50) - D = 0


    here A, B and C all would be positive so that function is monotonic.
    Solution is guaranteed to exist somewhere in range 0 <= x <= 100.

    Solution should be calculated with precision 0.0000001 = 1e-7 or better.

    Input data will contain number of test-cases in the first line.
    Next lines will contain four numbers for each test-case, i.e. A B C D
    separated by values. Answer should contain solutions - i.e. values of x
    which satisfy equation with given coefficients - several answers (for
    several test-cases) should be separated with spaces.
    :return:
    """


def stringToFloat():
    """
    This function open .csv values.
    :return:
    """
    arq = open("problem034.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = float(l1[i][k])
        l2.append(l1[i])
        l1[i] = []
    print(l2)
    return l1


def binarySearch(l2):
    l3 = []
    for i in range(0, 1_000_000):
        for k in range(0, len(l2[i])):
            if l2[i][k] * i + l2[i][k + 1] * sqrt(i ** 3) - l2[i][k + 2] * exp(-i / 50) - l2[i][i + 3] == 0:
                l3.append(i)
                break
    return l3


binarySearch(stringToFloat())
