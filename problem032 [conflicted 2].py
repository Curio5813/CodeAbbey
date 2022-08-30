from csv import reader
from time import sleep


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
    n, k, l2 = l1[0], l1[1], []
    for i in range(1, n + 1):
        l2.append(i)
    for i in range(1, 9):
        for k in range(0, len(l2), l1[1]):
            print(l2)
            if k > len(l2) - 1:
                k -= len(l2)
            l2.pop(k - 1)
            k += 2
    return print(*l2)


josephusProblem()  # dados: 44 8, answer: 38
