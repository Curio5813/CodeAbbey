from csv import reader


def stringToInteger():
    """
    This function open .csv file and return a list of integer.
    :return:
    """
    arq = open("problem067.csv")
    l1 = reader(arq)
    l1 = list(l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(*l2)
        l2 = []
    return l3


def fibonacciSequence(l3):
    """
    This function calculate the fibonacci sequence and has the return
    the index to each fibonacci's numbers from the list above.
    :param l3:
    :return:
    """
    print(l3)
    l5, l4, a, b, p = [], [], 0, 1, 1
    for i in range(0, 100_000):
        l4.append(a)
        a, b = b, p
        p = a + b
    for i in range(0, len(l3)):
        if l3[i] in l4:
            idx = l4.index(l3[i])
            l5.append(idx)
    return print(*l5)


fibonacciSequence(stringToInteger())
