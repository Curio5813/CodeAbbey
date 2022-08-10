from csv import reader


def justBrackets():
    """
    This function open a .csv file and return a list of strings.
    :return:
    """
    arq = open("problem019.csv")
    l1 = reader(arq)
    l1 = list(l1)
    l2, l3 = "", []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            for m in range(0, len(l1[i][k])):
                if l1[i][k][m] in "()[]{}<>":
                    l2 += l1[i][k][m]
            l3.append(l2)
            l2 = ""
    print(l3)
    return l3


def matchingBrackets(l3):
    """
    This function take the two parameter, list with strings, given
    by above function and return 1 if it's matching or 0 if not.
    :return:
    """
    cont1, cont2 = 0, 0
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            if l3[i][k] in "([{<":
                asw = 1
                cont1 += 1
            elif l3[i][k] in ")]}>":
                asw = 0
                cont2 += 1


    return print(*lsw)


matchingBrackets(justBrackets())
