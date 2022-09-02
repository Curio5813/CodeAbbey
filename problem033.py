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
    print(l1)
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
    This function opens a .csv file and return a string if numbers.
    """
    arq3 = open("problem033-data.csv")
    l3 = reader(arq3, delimiter=" ")
    l3 = list(*l3)
    for i in range(0, len(l3)):
        l3[i] = int(l3[i])
    return l3


def convertAsciiToBinary(l3):
    """
    This function opens a .csv files and has the return a list of
    string represented in binary base.
    :return:
    """
    l4, l5, l6 = [], "", []
    for i in range(0, len(l3)):
        l4.append(bin(l3[i]))
        l5 = "" + l4[i][2:]
        l6.append(l5)
    return l6


def parityControl(l6):
    """
    This function take a list of binary number, given from the
    function above and return a list of the binary fixing it when
    losing bits in broadcasting.
    :param l6:
    :return:
    """
    l7, l8, l9 = "", [], []
    for i in range(0, len(l6)):
        for k in range(0, len(l6[i])):
            if l6[i].count("1") % 2 != 0:
                if l6[i][k] == "1":
                    l7 = "0" + l6[i][1:]
                    l8.append(int(l7, 2))
                    break
                elif l6[i][k] == "0":
                    l7 = "0" + l6[i][:]
                    l8.append(int(l7, 2))
                    break
            else:
                l7 = l6[i]
                l8.append(int(l7, 2))
                break
    return l8


def asciiChart(l8, l1, l2):
    """
    This function return the charters in latin letter from the list
    given by the function above with the Ascii code.
    :param l8:
    :param l2:
    :return:
    """
    print(l8)
    name = ""
    for i in l8:
        for k in l1:
            if i in l1:
                name += l2[l1.index(i)]
    return print(name)


asciiChart(parityControl(convertAsciiToBinary(stringToData())), stringToAscii(), stringToChart())
