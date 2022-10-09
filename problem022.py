from csv import reader


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
    print(l1)
    cont, l2, soma = 0, [], 0
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            t1 = l1[i][2] / l1[i][0]
            t2 = l1[i][2] / l1[i][1]
            total = t1 - t2
        l2.append(total)
    return print(*l2)


twoPrinters(stringToInteger())
