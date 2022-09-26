from csv import reader


def secretNumber():
    """
    This function return a list of four digits of a secret
    number given in this task.
    :return:
    """
    arq = open("problem059-01.csv")
    l1 = reader(arq)
    l1 = list(*l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(l1[i][k])
    return l2


def stringToInterge():
    """
    This function open a .csv file and return a list of integers.
    :return:
    """
    l4, l5 = [], []
    arq = open("problem059-02.csv")
    l3 = reader(arq, delimiter=" ")
    l3 = list(*l3)
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            l4.append(l3[i][k])
        l5.append(l4)
        l4 = []
    return l5


def bullsAndCows(l2, l5):
    """
    This function receive the parameters given by functions above
    and return the numbers of guesses given to discover the secret
    number.
    :param l2:
    :param l5:
    :return:
    """
    cont1, cont2, cont3 = 0, 0, 0
    for i in range(0, len(l5)):
        for k in range(0, len(l5[i])):
            if l5[i][k] in l2 and l2.index(l5[i][k]) == k:
                cont1 += 1
            elif l5[i][k] in l2 and l2.index(l5[i][k]) != k:
                cont2 += 1
            elif l5[i][k] not in l2:
                continue
        print(f"{cont1}-{cont2}", end=" ")
        cont1 = 0
        cont2 = 0


bullsAndCows(secretNumber(), stringToInterge())
