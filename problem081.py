from csv import reader


def bit_count():
    """
    This function open a .csv file with integer number and convert it all
    to a binary number. Then print the numbers of 1 in each binary numbers
    converted. To negative integer use the complement of 2 to convert binary
    numbers with signal in a negative binary numbers.
    P.S.: The number of bit is equal to the number of "1" and that represent
    the integer number in binary numeric system.
    :return:
    """
    # This snippet of the code open the .csv files with the datas
    # of the program and put into a list.
    arq = open("problem081.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    # This snippet of the code convert the integer numbers in binary
    # and put it into a list.
    l2, positivo, negativo, invertido, bit, bits, qt_bits, n1, n2 = [], [], [], [], "", [], [], 0, 0
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
        l2.append(bin(l1[i]))
    # This snippet of the code divide positive binary's number from negative
    # into a two different lists.
    for i in range(0, len(l2)):
        if l2[i][0] == "0":
            l2[i] = l2[i][2::]
            positivo.append(l2[i])
        elif l2[i][0] == "-":
            l2[i] = l2[i][3::]
            negativo.append(l2[i])
            l2[i] = l2[i][::-1]
            invertido.append(l2[i])
    # This snippet of the code use the complement of 2 to
    # to convert binary numbers with signal in negative
    # binary numbers.
    for i in range(0, len(negativo)):
        for k in range(0, len(negativo[i])):
            while invertido[i][k] != "1":
                bit = "0" + bit
                k += 1
            else:
                if k == 0:
                    bit = "1"
                    k += 1
                elif k > 0:
                    bit = "1" + bit
                    k += 1
                while k <= len(invertido[i]) - 1:
                    if invertido[i][k] == "1":
                        bit = "0" + bit
                    elif invertido[i][k] == "0":
                        bit = "1" + bit
                    k += 1
            bits.append(bit)
            bit = ""
            break
    # This snippet of the code count how many 1 have in each
    # binary numbers and put in a list that in the end of the
    # program will print the quantitive of 1 for each binary.
    for i in range(0, len(l1)):
        if l1[i] >= 0:
            a = positivo[n1].count("1")
            qt_bits.append(a)
            n1 += 1
        elif l1[i] < 0:
            tam_negativo = 32 - len(bits[n2])
            b = tam_negativo + bits[n2].count("1")
            qt_bits.append(b)
            n2 += 1
    print(*qt_bits)


bit_count()
