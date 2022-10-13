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
    l2 = reader(arq2, delimiter=",")
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
    string represented in binary number.
    :return:
    """
    b, l4 = "", []
    for i in range(0, len(l3)):
        b = bin(l3[i]).replace("0b", "")
        b = b[::-1]
        while len(b) < 8:
            b += "0"
        b = b[::-1]
        l4.append(b)
    return l4


def parityControl(l4):
    """
    This function take a list of binary number, given from the
    function above and return a list of the binary fixing it when
    loses bits in broadcasting, and excluding the corrupted bytes.
    :param l4:
    :return:
    """
    l5 = []
    for i in range(0, len(l4)):
        # Doing the Parity Control, excluding the binary number with odd numbers of bits.
        if l4[i].count("1") % 2 == 0:
            if l4[i][0] == "1":
                l4[i] = "0" + l4[i][1:]
                l5.append(l4[i])
            elif l4[i][0] == "0":
                l5.append(l4[i])
    return l5


def asciiChart(l5, l2, l1):
    """
    This function return the charters in latin letter and it's digits from the lists
    given by the functions above using the Ascii code.
    :param l5:
    :param l2:
    :param l1:
    :return:
    """
    l6, l7, name, phrase = [], [],  "", ""
    for i in range(0, len(l5)):
        # Change the binary number to decimal number.
        num = int(l5[i], 2)
        l6.append(num)
    for i in range(0, len(l6)):
        if l6[i] in l1:
            # Use the decimal number took from above and use it in Ascii code.
            name += l2[l1.index(l6[i])]
    return print(name)


asciiChart(parityControl(convertAsciiToBinary(stringToData())), stringToChart(), stringToAscii())
