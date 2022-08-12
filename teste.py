from csv import reader
from statistics import mean, mode


def justBrackets():
    """
    This function open a .csv file and return a list of strings.
    :return:
    """
    arq = open("test.csv")
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
    print(*l3)
    return l3


def attributingToBracketsID(l3):
    """
    This function take the parameter, list with strings, given
    by above function and return a list of id to all kind of
    brackets.
    :return:
    """
    asw, l4 = "", []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            if l3[i][k] == "(":
                asw += "1"
            elif l3[i][k] == "[":
                asw += "2"
            elif l3[i][k] == "{":
                asw += "3"
            elif l3[i][k] == "<":
                asw += "4"
            if l3[i][k] == ")":
                asw += "1"
            elif l3[i][k] == "]":
                asw += "2"
            elif l3[i][k] == "{":
                asw += "3"
            elif l3[i][k] == "<":
                asw += "4"
        l4.append(asw)
        asw = ""
    print(*l4)
    return l4


def workingWithBracketsId(l4):
    """
    The function matching and return 1 if the brackets are
    all matching or 0 if nothing.
    :param l4:
    :return:
    """
    asw, lw, lw2 = 0, [], []
    for i in range(0, len(l4)):
        for k in range(0, len(l4[i])):
            halflen = int((len(l4[i]) / 2))
            hdown = l4[i][0:halflen]
            hup = l4[i][halflen:-1]
            print(hdown)
            print(hup)
            if len(l4[i]) % 2 != 0:
                asw = 0
                lw.append(asw)
                break
            else:
                if l4[i][k] == l4[i][k + 1]:
                    continue
                elif l4[i][k] != l4[i][k + 1]:
                    if l4[i][k + 1] == l4[i][k + 2]:
                        continue
                    if cont % 2 == 0:
                        asw = 1
                        lw.append(asw)
                        break
                    elif cont % 2 != 0:
                        asw = 0
                        lw.append(asw)
                        break
        lw2.append(*lw)
        lw = []
    return print(*lw2)


workingWithBracketsId(attributingToBracketsID(justBrackets()))
