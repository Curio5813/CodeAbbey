from csv import reader


def stringToList():
    """
    This function take a .csv file and put it in a list of strings.
    :return:
    """
    arq = open("problem020.csv")
    l1 = reader(arq)
    l1 = list(l1)
    str1, str2 = "", []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            str1 += l1[i][k]
        str2.append(str1)
        str1 = ""
    return str2


def vowelCount(str2):
    """
    This function take a list from the function above and count
    the number of vowel every string has.
    :param str2:
    :return:
    """
    cont, l2 = 0, []
    for i in range(0, len(str2)):
        for k in range(0, len(str2[i])):
            if str2[i][k] in "aeiouy":
                cont += 1
        l2.append(cont)
        cont = 0
    return print(*l2)


vowelCount(stringToList())
