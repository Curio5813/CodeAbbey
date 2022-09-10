from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of integer.
    :return:
    """
    arq = open("problem081.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    l2 = []
    for i in l1:
        i = int(i)
        l2.append(i)
    return l2


def fromIntegerToBinary(l2):
    """
    This function take a parameter with a list of integer,
    transform it in binary numbers and put it in a list.
    :param l2:
    :return:
    """
    print(l2)
    n, num, l3 = "", "", []
    for i in range(0, len(l2)):
        n_b = bin(l2[i]).replace("b", "").replace("-", "")
        # I used this as shown from the example to get the number -1 in the binary system.
        if l2[i] == -1:
            l3.append("11111111111111111111111111111111")
        # I'm trying to get the binary negative number using 2's complement method.
        elif l2[i] < 0:
            n_b = bin(l2[i]).replace("-0b", "")
            n_b = n_b[::-1]
            n_b = "1" + n_b
            num_1 = 31 - len(n_b)
            for k in range(0, num_1 + 1):
                num += "0"
            n_b = n_b + num
            print(len(n_b))
            l3.append(n_b)
            num = ""
        else:
            l3.append(n_b)
    return l3


def bitCount(l3):
    """
    This function take a parameter with a list of binary numbers
    from the function above and count in binary system how many bits
    is in each binary number.
    P.S.: The number of bit is equal to the number of "1" in that
    represent the integer number in binary system.
    :param l3:
    :return:
    """
    print(l3)
    cont, l4 = 0, []
    for i in range(0, len(l3)):
        cont = l3[i].count("1")
        l4.append(cont)
    return print(*l4)


bitCount(fromIntegerToBinary(stringToInteger()))
