from csv import reader
from time import time


start = time()


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
    parameter and return a list of numbers to resolver the
    classical problem of the two printers.
    :param l1:
    :return: 
    """
    for i in range(0, len(l1)):
        cont, soma, n1, n2 = 0, 0, 1, 1
        while soma < l1[i][2]:
            cont += 1
            if cont == l1[i][0] * n1:
                soma += 1
                n1 += 1
                if soma == l1[i][2]:
                    print(f"{cont}", end=" ")
                    break
            if cont == l1[i][1] * n2:
                soma += 1
                n2 += 1
                if soma == l1[i][2]:
                    print(f"{cont}", end=" ")
                    break


twoPrinters(stringToInteger())
end = time()
print(f"{(end - start):.3f}")
