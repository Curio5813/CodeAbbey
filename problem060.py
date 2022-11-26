from csv import reader


def stringToInteger():
    """
    This function open a csv file and return a list of integers.
    :return:
    """
    arq = open("problem060.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    print(l1)
    return l1


def sweetHarvest(l1):
    """
    This function takes a parameter given to the above function
    and returns the maximum possible amount of collected candies
    by the rabbit.
    :param l1:
    :return:
    """
    cont, l2, l3 = 0, [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if k >= len(l1[i]) - 3:
                break
            if l1[i][k + 2] > l1[i][k + 3]:
                cont += l1[i][k + 3]
                l3.append(l1[i][k + 3])
            elif l1[i][k + 3] < l1[i][k + 2]:
                cont += l1[i][k + 2]
                l3.append(l1[i][k + 2])
        l2.append(cont)
        print(l3)
        cont = l1[0][0]
    return print(*l2)


sweetHarvest(stringToInteger())
