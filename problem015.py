from csv import reader


def stringToInteger():
    """
    This function convert string to integer values and return
    a list with them.
    :return:
    """
    l2 = []
    arq = open("problem015.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(int(l1[i][k]))
    return l2


def minAndMaxValues(l2):
    """
    This function return the minimum and maximum from a list given by
    function above
    :return:
    """
    return print(f"{max(l2)} {min(l2)}")


minAndMaxValues(stringToInteger())
