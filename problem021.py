from csv import reader


def arrayCounters():
    """
    This function open a .csv file and put them in a list of integer and
    return how many times the numbers appear into list.
    :return:
    """
    arq = open("problem021.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    l2, cont, l3 = [], 0, []
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
        l2.append(l1[i])
    l2.sort()
    for i in range(1, 21):
        a = (l2.count(i))
        l3.append(a)
        if a == 0:
            l3.pop()
    return print(*l3)


arrayCounters()
