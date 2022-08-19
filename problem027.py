from csv import reader


def stringToInteger():
    """
    This function takes a .csv file which has a list of string
    and return a list of integer numbers.
    :return:
    """
    arq = open("problem027.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def bubbleSort(l1):
    """
    This function takes a list of integer numbers generated from the
    function above and return the number of swaps and performance
    made to order the list.
    :param l1:
    :return:
    """
    i, cont1, cont2 = 0, 0, 2
    l2 = l1.copy()
    l1.sort()
    while l2 != l1:
        while l2[i] > l2[i + 1]:
            l2[i], l2[i + 1] = l2[i + 1], l2[i]
            cont1 += 1  # This calculates the number of swaps made.
        else:
            i += 1
            if i >= len(l1) - 1:
                i = 0
                cont2 += 1  # This calculates the number of performance made,
                # include the initial state and final state.
    print(f"{cont2} {cont1}")


bubbleSort(stringToInteger())
