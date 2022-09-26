from math import factorial
from csv import reader


def strintToInteger():
    """
    This function open a .csv file and return a lists of
    integers.
    :return:
    """
    arq = open("problem128.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    print(l1)
    return l1


def combinationsCounting(l1):
    """
    This function take a parameter given by the function above
    and return the combinations of each n elements combained
    k to k.
    :param l1:
    :return:
    """
    comb, l2 = 0, []
    for i in range(0, len(l1)):
        for j in range(0, len(l1[i])):
            n = l1[i][j]
            k = l1[i][j + 1]
            comb = factorial(n) / ((factorial(n - k)) * factorial(k))
            break
        l2.append(int(comb))
    return print(*l2)


combinationsCounting(strintToInteger())
