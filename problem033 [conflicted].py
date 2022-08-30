from csv import reader


def stringToAscii():
    """
    This function open a .csv files and has the return a list of
    Ascii code.
    """
    arq1 = open("problem033-ascii.csv")
    l1 = reader(arq1, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def stringToChart():
    """
    This function open a .csv files and has the return a list of a
    Ascii Character.
    """
    arq2 = open("problem033-chart.csv")
    l2 = reader(arq2, delimiter=" ")
    l2 = list(*l2)
    return l2


def stringToData():
    """
    This function open a .csv files and has the return a list of data
    given.
    """
    arq3 = open("problem033-data.csv")
    l3 = reader(arq3, delimiter=" ")
    l3 = list(*l3)
    print(l3)
    return l3


def convertAsciiToBinary(l3):
    """
    This function convert code in Ascii to Binary from the list l3
    given by above function.
    :return:
    """
    l4, l5, k = [], [], 0
    for i in range(0, len(l3)):
        while int(l3[i]) // 2 != 0:
            l3[i] = int(l3[i])
            print(int(l3[i]))
            l3[i] %= 2
            rem = l3[i].append(l3[i])
        print(rem)
        l3[i] = int(l3[i])
        l4.append(bin(l3[i]))
        print(l4[i])
        if l4[i].count("0") % 2 == 0 and l4[i].count("1") % 2 == 0:
            l4[i].replace("0b", "")
        else:
            l4[i].replace("0b0", "1")
    print(l4)
    return l4


def parityControl(l4):
    """
    This function take a list fo binary number, given from the
    function above and return a list of Ascii Code.
    :param l4:
    :param l1:
    :param l2:
    :return:
    """
    l5, n = [], 0
    for i in range(0, len(l4)):
        print(l4)
        if l4[i].count("0") % 2 == 0 and l4[i].count("1") % 2 == 0:
            l5.append(int(l4[i], 2))
            print(l5)
        else:
            l4[i][0].replace("0", "")
            c = "1" + l4[i][2:]
            print(c)
            l5.append(int(c, 2))
    print(*l5)
    return l5


def asciiChart(l5):
    """
    This function return the charters in latin letter from the list
    given by the function above with the Ascii code.
    :param l5:
    :return:
    """
    for i in range(0, len(l5)):
        print("ok")
        break


parityControl(convertAsciiToBinary(stringToData()))
