from csv import reader


def stringToInteger():
    """
    This function open a .csv files ans convert string to integer variable,
    and return a list that which is a timestamps.
    :return:
    """
    arq = open("problem012.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    return l1


def transformAllToSeconds(l1):
    """
    This function take the parameter given by the function above
    and return with another list all values in seconds.
    :param l1:
    :return:
    """
    diff, l2 = 0, []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            d1 = l1[i][0] * 24 * 60 * 60
            h1 = l1[i][1] * 60 * 60
            m1 = l1[i][2] * 60
            s1 = l1[i][3]
            d2 = l1[i][4] * 24 * 60 * 60
            h2 = l1[i][5] * 60 * 60
            m2 = l1[i][6] * 60
            s2 = l1[i][7]
            t1 = d1 + h1 + m1 + s1
            t2 = d2 + h2 + m2 + s2
            diff = t2 - t1
        l2.append(diff)
    return l2


def moduloAndTimeDifference(l2):
    """
    This function return a list with the time difference
    :return:
    """
    for i in range(0, len(l2)):
        day = l2[i] // (24 * 60 * 60)
        l2[i] = l2[i] - (day * 24 * 60 * 60)
        hrs = l2[i] // (60 * 60)
        l2[i] = l2[i] - (hrs * 60 * 60)
        minut = l2[i] // 60
        l2[i] = l2[i] - (minut * 60)
        second = l2[i]
        print(f"({day} {hrs} {minut} {second})", end=" ")


moduloAndTimeDifference(transformAllToSeconds(stringToInteger()))
