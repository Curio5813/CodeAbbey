from csv import reader


def stringsToListofStrings():
    """
    This function open a .csv file and return a list of strings.
    In that list fo strings case of the letters is ignored.
    Spaces and punctuations are ignored too.
    :return:
    """
    arq = open("problem050.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    str_l, l2, l3 = "", [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):  # This loop remove everything that is not a letter
            str_l += l1[i][k].replace(",", "").replace(".", "").\
                replace("!", "").replace("?", "").replace("-", "").replace("'", "")
        l2.append(str_l.lower())
        str_l = ""
    print(l2)
    return l2


def palindromes(l2):
    """
    This function takes the list l2, given by the function above
    and print for each string if it is a palindrome 'Y', or not, 'N'.
    :return:
    """
    l3 = []
    for i in range(0, len(l2)):
        if l2[i] == l2[i][::-1]:
            l3.append("Y")
        elif l2[i] != l2[i][::-1]:
            l3.append("N")
    print(len(l3))
    return print(*l3)


palindromes(stringsToListofStrings())
