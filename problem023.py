from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of integers.
    :return:
    """
    arq = open("problem023.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    l1.pop()  # This method remove from the list the last term.
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def bubbleInArray(l1):
    """
    This function moves some greater elements right (to the
    end of array) and some smaller elements left (to the
    beginning). What is the most important: the largest element
    is necessarily moved to the last position and then makes
    checksum from the data.
    :param l1:
    :return:
    """
    soma, cont = 0, 0
    for i in range(0, len(l1)):
        if i >= len(l1) - 1:
            break
        if l1[i] > l1[i + 1]:
            l1[i], l1[i + 1] = l1[i + 1], l1[i]
            cont += 1
        else:
            continue
    for i in range(0, len(l1)):
        soma += l1[i]
        soma *= 113
        soma %= 10000007
    return print(f"{cont} {soma}")


bubbleInArray(stringToInteger())
