from csv import reader


def stringToInteger():
    """
    This function open a .csv file with list of strings and
    return a list of integer.
    :return:
    """
    arq = open("problem024.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def neumannRandomGenerator(l1):
    """
    This function take the list from the above function and
    does the math operations to generator numbers pseudorandom.
    The function return the number of step before it enter in a
    infinite loop.
    :param l1:
    :return:
    """
    gen, l2, cont, l3 = 0, [], 0, []
    for i in range(0, len(l1)):
        while l1[i] not in l2:
            l2.append(l1[i])
            l1[i] **= 2
            l1[i] //= 100
            l1[i] %= 10_000
            cont += 1
        l3.append(cont)
        l2 = []
        cont = 0
    return print(*l3)


neumannRandomGenerator(stringToInteger())
