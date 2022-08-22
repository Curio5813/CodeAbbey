from csv import reader


def openCSVFile():
    """
    This function open a .csv file and put into a list with strings
    and numbera.
    :return:
    """
    arq = open("problem031.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][0] = int(l1[i][0])
    return l1


def rotateString(l1):
    """
    This function take a list of strings and numbers
    and rotate these strings in a specific way determined
    by their index.
    :param l1:
    :return:
    """
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            idx = l1[i][0]
            a = len(l1[i][1])
            if l1[i][1] and idx > 0:
                st1 = l1[i][1][0:idx]
                st2 = l1[i][1][idx:] + st1
                l2.append(st2)
                break
            elif l1[i][1] and idx < 0:
                idx *= -1
                st1 = l1[i][1][0:a - idx]
                st2 = l1[i][1][a - idx:] + st1
                l2.append(st2)
                break
    return print(*l2)


rotateString(openCSVFile())
