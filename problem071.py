from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list
    of integer.
    :return:
    """
    arq = open("problem071.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def fibonacciSequence():
    """
    This function return a Fibonacci Sequence until
    of stipulated limit.
    :return:
    """
    l2 = []
    a, b = 0, 1
    p = a + b
    for i in range(0, 180_000 + 1):
        l2.append(a)
        a, b = b, p
        p = a + b
    return l2


def fibonacciDivisibilityAdvanced(l1, l2):
    """
    Given usual Fibonacci Sequence, starting with 0 and 1:

            0 1 1 2 3 5 8 13 21 34 ...

    and some value M you will be asked to find the index of the
    first non-zero member of this list, which is evenly divisible
    by this M, e.g. if you are given M = 17 the answer is 9 (the
    index of the element 34).

    Input data in the first line will contain the number of test-cases.
    Next line will contain exactly this of divisors M (not exceeding 2_000_000)
    for which you should give answers. Answer should contain indices of
    members of Fibonacci Sequence, separated by spaces.
    :param l1:
    :param l2:
    :return:
    """
    l3 = []
    for i in l1:
        for k in l2[1:]:
            if k % i == 0:
                l3.append(l2.index(k))
                break
    print(*l3)


fibonacciDivisibilityAdvanced(stringToInteger(), (fibonacciSequence()))
