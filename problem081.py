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
    str_1, l3, idx = "", [], -1
    for i in range(0, len(l2)):
        n_b = bin(l2[i]).replace("0b", "").replace("-", "")
        t = 32 - len(n_b)
        for k in range(t):
            str_1 += "0"
        if l2[i] > 0:
            p_b = str_1 + n_b
            l3.append(p_b)
        elif l2[i] == -1:
            n_b = "11111111111111111111111111111111"
            l3.append(n_b)
        # Using the method complement of 2 for binary negative numbers
        elif l2[i] < -1:
            n_b = str_1 + n_b
            n_b = n_b.replace("1", "x").replace("0", "y")
            n_b = n_b.replace("x", "0").replace("y", "1")
            if n_b[-1] == "0":
                n_b[-1].replace("0", "1")
                l3.append(n_b)
            elif n_b[-1] == "1":
                n_b[-1].replace("1", "0")
                l3.append(n_b)
        str_1 = ''
    print(len(l3))
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
    cont, l4 = 0, []
    for i in range(0, len(l3)):
        cont = l3[i].count("1")
        l4.append(cont)
    return print(*l4)


bitCount(fromIntegerToBinary(stringToInteger()))


# Expected answer was:
# 22 8 12 11 13 22 26 29 7 17 15 28 17 26 11 20 10 10 20 26 11 9 5 28 21 17 23
# 5 19 18 22 12 15 22 14 13 14 4 7 17 20 26 29 17 7 14 30 19 10 4 12 15 8 29 12 7


# My answer was:
# length 56
# 21 8 12 11 13 23 25 28 7 20 15 28 21 25 11 19 10 10 19 26 11 9 5 27 21 16 23
# 5 19 18 22 12 14 21 14 13 14 4 7 16 19 30 28 19 7 14 31 18 10 4 12 15 8 28 12 7


