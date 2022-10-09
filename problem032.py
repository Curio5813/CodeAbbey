from csv import reader


def josephusProblem():
    """
    This function takes a classical programming puzzle.
    The Josephus Problem. This task is to determine for
    given number of people N and constant step K the
    position of a person who remains the last - i.e.
    the safe position. For example if there are 10 people,
    and they eliminate each third:
    :return:
    """
    arq = open("problem032.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    l1[0] = int(l1[0])
    l1[1] = int(l1[1])
    n, a, l2 = l1[0], l1[1], []
    for i in range(1, n + 1):
        l2.append(i)
    # This snippet of this code iterates into the list created and
    # pop the number from the list which is the multiple from a
    # given number excluding the number itself.
    while len(l2) > 1:
        while len(l2) > 1:
            # This snippet of the code iterate over the list until the value is
            # less than length of the list and the list have only one element.
            if a > len(l2):
                a -= len(l2)
                break
            else:
                # This snippet exclude the number in the list by gotten the
                # index above.
                l2.pop(a - 1)
                a += l1[1] - 1
    return print(*l2)


josephusProblem()
