from csv import reader


def bit_count():
    """
    This function take a parameter with a list of binary numbers
    from the function above and count in binary system how many bits
    is in each binary number.
    P.S.: The number of bit is equal to the number of "1" in that
    represent the integer number in binary system.
    :return:
    """
    arq = open("problem081.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    print(len(l1))
    print(*l1)
    l2, l3, pos, neg, n1, n2 = [], [], "", "", 0, 0
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
        l2.append(bin(l1[i]))
    print(*l2)
    for i in range(0, len(l2)):
        for k in range(0, len(l2[i])):
            if l2[i][0] == "0":
                len_p = 32 - len(l2[i][2::])
                while n1 < len_p:
                    pos += "0"
                    n1 += 1
                pos = pos + l2[i][2::]
                qt_ones = pos.count("1")
                print(qt_ones, end=" ")
                n1, pos = 0, ""
                break
            elif l2[i][0] == "-":
                len_n = 32 - len(l2[i][3:])
                while n2 < len_n:
                    neg += "0"
                    n2 += 1
                neg = neg + l2[i][3::]
                qt_ones = 32 - neg.count("1")
                print(qt_ones, end=" ")
                n2, neg = 0, ""
                break
    print("\n")


bit_count()
