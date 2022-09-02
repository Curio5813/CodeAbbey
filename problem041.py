from csv import reader


def medianOfThree():
    """
    This function open a .csv file, and it has the return a list with
    the medians of them.
    :return:
    """
    l2, l3 = [], []
    arq = open("problem041.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
            l2.sort()
        l3.append(l2[1])
        l2 = []
    return print(*l3)


medianOfThree()
