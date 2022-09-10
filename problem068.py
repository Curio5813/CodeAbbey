from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of
    integer.
    :return:
    """
    l2, l3 = [], []
    arq = open("problem068.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    return l3


def bicycleRace(l3):
    """
    This function take as parameter given the function above and
    return the distances between first city and rendezvous point.
    :param l3:
    :return:
    """
    sa, sb, t, l4 = 0, 0, 1, []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            dist, v1, v2 = l3[i][0], l3[i][1], l3[i][2]
            t = dist / (v1 + v2)  # This is the equation for Progressive Uniform Rectilinear Motion
            s = v1 * t
            l4.append(s)
            break
    return print(*l4)


bicycleRace(stringToInteger())
