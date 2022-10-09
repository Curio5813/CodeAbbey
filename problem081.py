from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of integer.
    :return:
    """
    arq = open("problem081.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def integerToBinary(l1):
    """
    This function take a parameter with a list of integer, from this
    the list take the positive integer numbers and transform it in binary
    numbers putted in a list the result it.
    :param l1:
    :return:
    """
    str_1, l2 = "", []
    for i in range(0, len(l2)):
        n_b = bin(l2[i]).replace("0b", "").replace("-", "")
        t = 32 - len(n_b)
        for k in range(t):
            str_1 += "0"
        if l2[i] > 0:
            p_b = str_1 + n_b
            l2.append(p_b)
        elif l2[i] == -1:
            n_b = "11111111111111111111111111111111"
            l2.append(n_b)
        # Using the method complement of 2 for binary negative numbers
        elif l2[i] < -1:
            n_b = str_1 + n_b
            n_b = n_b.replace("1", "x").replace("0", "y")
            n_b = n_b.replace("x", "0").replace("y", "1")
            if n_b[-1] == "0":
                n_b[-1].replace("0", "1")
                l2.append(n_b)
            elif n_b[-1] == "1":
                n_b[-1].replace("1", "0")
                l2.append(n_b)
        str_1 = ''
    print(len(l2))
    return l2


def bitCount(l2):
    """
    This function take a parameter with a list of binary numbers
    from the function above and count in binary system how many bits
    is in each binary number.
    P.S.: The number of bit is equal to the number of "1" in that
    represent the integer number in binary system.
    :param l2:
    :return:
    """
    cont, l3 = 0, []
    for i in range(0, len(l2)):
        cont = l2[i].count("1")
        l3.append(cont)
    return print(*l3)


bitCount(integerToBinary(stringToInteger()))


# 15 2 13 30 7 12 29 28 5 10 26 12 8 21 21 7 26
# 2 26 6 18 26 3 11 24 7 13 15 16 17 28 18 8 25 9 4 13 28 23 4
