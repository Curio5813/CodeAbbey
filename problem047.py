from csv import reader


def alphabetLetters():
    """
    This function return a list with the letters of the latin
    alphabet.
    :return:
    """
    l1 = []
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in alp:
        l1.append(i)
    return l1


def stringToStringApp():
    """
    This function open a .csv file and has the return the
    same string into a list.
    :return:
    """
    arq = open("problem047.csv")
    lx = reader(arq, delimiter="\n")
    lx = list(lx)
    l2 = []
    for i in range(0, len(lx)):
        for k in range(0, len(lx[i])):
            for j in range(0, len(lx[i][k])):
                l2.append(lx[i][k][j])
    return l2


def caesarShiftCipher(l1, l2):
    """
    This function will contain an integers, k, the key to encryption. The
    following lines will contain encrypted text, consisting of capital latin
    letters A ... Z, each line is terminated with a dot '.' which should
    not be decoded. Answer should contain the decrypted message (in a single
    line, no line splitting is needed).
    :param l1:
    :param l2:
    :return:
    """
    num1 = int(input("The Key Password: "))
    l3, str_c, l4 = [], "", []
    #  In this loop is set the rule of  the encryption
    for i in range(num1, len(l1)):
        l3 = l1[num1:] + l1[0:num1]
    for i in l2:
        if i == ".":
            l4.append(i)
            s = " "
            l4.append(s)
        elif i == ' ':
            l4.append(i)
        else:
            idx = l3.index(i) - num1
            l4.append(l3[idx])
    for i in l4:
        str_c += i
    return print(str_c)


caesarShiftCipher(alphabetLetters(), stringToStringApp())
