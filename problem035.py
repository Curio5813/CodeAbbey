from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of integer.
    :return:
    """
    arq = open("problem035.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    return l3


def savingsCalculator(l3):
    """
    This function take a list of datas from the function above and
    calculate how many years the investor have to save to will have
    enough money to pay your desire as a consumer.
    :param l3:
    :return:
    """
    cont, l4 = 0, []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            sav = l3[i][0]
            mont = l3[i][1]
            while sav <= mont:
                rat = (l3[i][2] / 100) + 1  # It is a compound capitalization.
                sav *= rat
                sav = round(sav, 2)
                cont += 1
            l4.append(cont)
            break
        cont = 0
    return print(*l4)


savingsCalculator(stringToInteger())
