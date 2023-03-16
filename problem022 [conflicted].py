from csv import reader
from time import sleep


def stringToInteger():
    """
    This function open a .csv file wich a list of strings
    and return a list of integer.
    :return:
    """
    arq = open("problem022.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    return l1


def twoPrinters(l1):
    """
    This function take a list given function above as
    parameter and return a list of numbers to solve the
    classical problem of the two printers.
    :param l1:
    :return: 
    """
    cont, pg, l2 = 0, 0, []
    for i in range(0, len(l1)):
        while True:
            cont += 1
            if cont % l1[i][0] == 0:
                pg += 1
                if pg == l1[i][2]:
                    l2.append(cont)
                    break
            if cont % l1[i][1] == 0:
                pg += 1
                if pg == l1[i][2]:
                    l2.append(cont)
                    break
        cont, pg = 0, 0
    return print(*l2)


twoPrinters(stringToInteger())
