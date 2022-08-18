from csv import reader


def stringToInteger():
    """
    This function convert a string to a integer and return a list
    with them.
    :return:
    """
    arq = open("problem023.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
    return l2


def arrayChecksum(l2):
    """
    This function take a array from the function above as
    parameter and calculate the checksum by doing for each
    element of the array (starting from beginning) add this
    element to result variable and multiply this sum by 113.
    This new value taken by modulo 10000007 should become
    the next value of result, and so on.
    :param l2:
    :return:
    """
    print(l2)
    soma = 0
    for i in range(0, len(l2)):
        soma += l2[i]
        soma *= 113
        soma %= 10000007
    return print(soma)


arrayChecksum(stringToInteger())
