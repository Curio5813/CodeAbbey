from csv import reader


def stringToInteger():
    """
    This function take a list of strings and return a list o integer.
    :return:
    """
    arq = open("problem022.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            num = int(l1[i][k])
            l2.append(num)
        l3.append(l2)
        l2 = []
    print(l3)
    return l3


def twoPrinters(l3):
    """
    This function take a list above from given function as
    parameter and return a list of numbers to resolver the
    classical problem of the two printers.
    :param l3: 
    :return: 
    """
    cont, pg, l4 = 0, 0, []
    for i in range(0, len(l3)):
        while pg < l3[i][2]:
            cont += 1
            if cont % l3[i][0] == 0:
                pg += 1
            if cont % l3[i][1] == 0:
                pg += 1
        l4.append(cont)
        cont, pg = 0, 0
    return print(*l4)


twoPrinters(stringToInteger())
