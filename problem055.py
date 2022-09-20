from csv import reader


def stringToListOfStrings():
    """
    This function open a .csv file and return a
    list with those strings.
    :return:
    """
    arq = open("problem055.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    return l1


def decrypt(l1):
    """
    This function takes the parameter given by function above
    and decrypts the text to enter into the cave with treasures.
    The return a list of words.
    :param l1
    :return:
    """
    n, word, l2 = 0, 0, []
    for i in l1:
        n = l1.count(i)
        if n > 1 and i not in l2:
            l2.append(i)
    l2.sort()
    return print(*l2)


decrypt(stringToListOfStrings())
