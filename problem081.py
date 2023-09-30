from csv import reader


def bit_count():
    """
    This function take an integer number and convert it to a binary number.
    Then print the numbers of ones in each binary numbers converted. To
    negative integer use the complement of 2 when convert it to binary numbers.
    P.S.: The number of bit is equal to the number of "1" in that
    represent the integer number in binary system.
    :return:
    """
    arq = open("problem081.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    l2, positivo, negativo, invertido, bit, bits, qt_bits, n1, n2 = [], [], [], [], "", [], [], 0, 0
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
        l2.append(bin(l1[i]))
    for i in range(0, len(l2)):
        if l2[i][0] == "0":
            l2[i] = l2[i][2::]
            positivo.append(l2[i])
        elif l2[i][0] == "-":
            l2[i] = l2[i][3::]
            negativo.append(l2[i])
            l2[i] = l2[i][::-1]
            invertido.append(l2[i])
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
