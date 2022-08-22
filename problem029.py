from csv import reader


def stringToInteger():
    """
    This function open a csv file  and return a list of integer numbers.
    :return:
    """
    arq = open("problem029.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def sortWithIndexes(l1):
    """
    This function takes the parameters given for the function above
    and print a list of index the existed was before the list get
    ordered.
    :param l1: 
    :return: 
    """
    print(l1)
    l2 = []
    for i in range(0, len(l1)):
        minu = l1.index(min(l1))
        l2.append(minu + 1)
        l1.insert(minu, 1_000_000)
        l1.pop(minu + 1)
        print(l1)
    return print(*l2)


sortWithIndexes(stringToInteger())
