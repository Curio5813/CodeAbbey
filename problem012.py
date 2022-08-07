from csv import reader
from datetime import timedelta


def stringToInteger():
    """
    This function convert string to integer variable, and return
    a list that which is a timestamps.
    :return:
    """
    arq = open("problem012.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    return l1


def moduloAndDifference(l1):
    """
    This function take the parameter given by the function above
    and return a list with the differnce beteewn the timestamps
    give above in a list.
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
    print(l2)


moduloAndDifference(stringToInteger())
