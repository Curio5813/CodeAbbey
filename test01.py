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
    n = l1[0]
    b = l1[1]
    l2, a = [], 1
    for i in range(1, n + 1):
        l2.append(i)
    print(l2)
    sleep(1)
    for i in range(0, len(l2)):
        if len(l2) == 1:
            break
        for k in range(b - a, len(l2), b - 1):
            print(k)
            sleep(2)
            if len(l2) == 1:
                break
            if k >= len(l2) - 1:
                break
            l2.pop(k)
            print(l2)
            sleep(1)
        a += 1
    return print(*l2)


josephusProblem()  # dados: 44 8, answer: 38
