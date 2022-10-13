from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of integer.
    :return:
    """
    arq = open("problem120.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def selectionSort(l1):
    """
    This function take a list of integer given by the function
    above and return a minimum value of the list using the Selection
    Sort algorithm.
    :param l1:
    :return:
    """
    n, l_idx = 0, []
    for i in range(0, len(l1) - 1):
        idx = l1.index(max(l1))
        l_idx.append(idx)
        l1[idx], l1[-1] = l1[-1], l1[idx]
        l1.pop()
    return print(*l_idx)


selectionSort(stringToInteger())
