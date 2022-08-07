from csv import reader


def stringsToInteger():
    """
    This function take the datas from a .csv in string file
    to convert to integer.
    :return:
    """
    arq = open("problem011.csv")
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


def operationsIfTheData(l3):
    """
    This function has as retunr the operations with the three number given
    by the "l3" list, wich the first is multipled by second and the result of
    mutiplicantion is add to third number into list.
    :param l3:
    :return:
    """
    somas, soma = [], 0
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            mult = l3[i][0] * l3[i][1]
            soma = mult + l3[i][2]
        somas.append(soma)
    return somas


def sumOfDigits(somas):
    """
    This function return the sum of the digits that is used by
    the integer numbers given by the list "somas".
    :param somas:
    :return:
    """
    l4, l5 = [], []
    for i in range(0, len(somas)):
        while somas[i] > 0:
            c = somas[i] % 10
            l4.append(c)
            somas[i] //= 10
        l5.append(sum(l4))
        l4 = []
    return print(*l5)


sumOfDigits(operationsIfTheData(stringsToInteger()))
