from csv import reader


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
    print(l3)
    print(len(l3))
    return l3


def matchingBrackets(l3):
    """
    This function take the two parameter, list with strings, given
    by above function and return 1 if it's matching or 0 if not.
    :return:
    """
    brkop = ["(", "[", "{", "<"]
    n1 = [0, 1, 2, 3]
    brkcl = [")", "]", "}", ">"]
    n2 = [0, 1, 2, 3]
    cont1, cont2, cont3, cont4, l4 = [], [], [], [], []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            if l3[i][k] in brkop:
                asw = brkop.index(l3[i][k])
                cont1.append(n1[asw])
            elif l3[i][k] in brkcl:
                asw = brkcl.index(l3[i][k])
                cont2.append(n2[asw])
        cont3.append(cont1)
        cont4.append(cont2)
        cont1 = []
        cont2 = []
    print(*cont3)
    print(*cont4)
    for i in range(0, len(cont3)):
        if cont3[0] == cont4[-1] and cont3[i]:  # Prosseguir daqui!
            cont = 0
            l4.append(cont)
        else:
            cont = 1
            l4.append(cont)
    print(*l4)  # 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 0 0 0


matchingBrackets(justBrackets())
