from csv import reader
from time import sleep


def justBrackets():
    """
    This function open a .csv file and return a list of strings.
    :return:
    """
    arq = open("test01.csv")
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


def attributingToBracketsId(l3):
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
    asw, lw, lw2, cont = 0, [], [], 0
    for i in range(0, len(l4)):
        for k in range(0, len(l4[i])):
            a = len(l4[i])
            b = a // 2
            if len(l4[i]) > 4:
                if l4[i][b - 1] == l4[i][b]:
                    l4[i] = l4[i].replace(l4[i][b - 1:b + 1], "")
                    b -= 1
                elif l4[i][b - 1] != l4[i][b]:
                    if l4[i][b - 2] == l4[i][b - 1] and l4[i][b] == l4[i][b + 1]:
                        l4[i] = l4[i].replace(l4[i][b - 2:b + 2], "")
                        b -= 1
                    elif l4[i][b - 2] != l4[i][b - 1] or l4[i][b] != l4[i][b + 1]:
                        break
            elif len(l4[i]) <= 4:
                if len(l4[i]) == 2:
                    if l4[i][0] == l4[i][1]:
                        l4[i] = l4[i].replace(l4[i][b - 1:b + 1], "")
                        b -= 1
                        break
                    elif l4[i][0] != l4[i][1]:
                        break
                if len(l4[i]) == 4:
                    if l4[i][b - 2] == l4[i][b - 1] and l4[i][b] == l4[i][b + 1]:
                        l4[i] = l4[i].replace(l4[i][b - 2:b + 2], "")
                        break
                    elif l4[i][b - 2] != l4[i][b - 1] or l4[i][b] == l4[i][b + 1]:
                        break
        if len(l4[i]) == 0:
            lw.append(1)
        else:
            lw.append(0)
    return print(*lw)  # 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 0 0 0


workingWithBracketsId(attributingToBracketsId(justBrackets()))
