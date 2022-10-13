from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of nested string.
    :return:
    """
    arq = open("problem036.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    return l1


def noNumber(l1):
    """
    This function take the parameter above and return a list with
    no guessed number.
    :param l1:
    :return:
    """
    l2, l3, l4 = [], [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if l1[i][1] == "0":
                l2.append(l1[i][k])
            break
    for i in range(0, len(l2)):
        for k in range(0, len(l2[i])):
            for m in range(0, len(l2[i][k])):
                l3.append(l2[i][k][m])
        l4.append(l3)
        l3 = []
    return l4


def oneNumber(l1):
    """
    This function take the parameter and return a list os string that
    was guessed one number.
    :param l1:
    :return:
    """
    l5, l6, l7 = [], [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if l1[i][1] == "1":
                l5.append(l1[i][k])
            break
    for i in range(0, len(l5)):
        for k in range(0, len(l5[i])):
            for m in range(0, len(l5[i][k])):
                l6.append(l5[i][k][m])
        l7.append(l6)
        l6 = []
    return l7


def twoNumbers(l1):
    """
    This function take the parameter and return a list os string that
    was guessed one number.
    :param l1:
    :return:
    """
    l8, l9, l10 = [], [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if l1[i][1] == "2":
                l8.append(l1[i][k])
            break
    for i in range(0, len(l8)):
        for k in range(0, len(l8[i])):
            for m in range(0, len(l8[i][k])):
                l9.append(l8[i][k][m])
        l10.append(l9)
        l9 = []
    return l10


def guesserNumbers(l4, l7, l10):
    """
    This function take the parameter and return a guessed number.
    :param l4
    :param l7
    :param l10
    :return
    """
    print(l4)
    print(l7)
    print(l10)
    g = []
    for i in range(0, len(l10)):
        if i >= len(l10) - 1:
            break
        for k in range(0, len(l10[i])):
            for m in range(0, len(l10[i][k])):
                if l10[i][k][m] == l10[i + 1][k][m]:
                    g.append(l10[i][k][m])


guesserNumbers(noNumber(stringToInteger()), oneNumber(stringToInteger()), twoNumbers(stringToInteger()))
