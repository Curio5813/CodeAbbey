from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of
    integer.
    :return:
    """
    arq = open("problem048.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def collatzSequence(l1):
    """
    This function take the list of integer from the function above and
    calculates for each number from the list the number of steps until
    to get the number 1 in Collatz's Conjecture.
    :param l1:
    :return:
    """
    cont, l2 = 0, []
    for i in range(0, len(l1)):
        while l1[i] > 1:
            if l1[i] % 2 == 0:
                l1[i] /= 2
                cont += 1
            elif l1[i] % 2 == 1:
                l1[i] = 3 * l1[i] + 1
                cont += 1
        l2.append(cont)
        cont = 0
    return print(*l2)


collatzSequence(stringToInteger())
