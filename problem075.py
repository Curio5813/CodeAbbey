from csv import reader
from collections import Counter


def strinToInteger():
    """
    This function open a csv file and return a list of integer.
    :return:
    """
    arq = open("problem075.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    print(l1)
    return l1


def yachtGame(l1):
    """
    This function take the parameter given by the functio above
    and retunr a list of string wich contain the name for each of
    combinations. Names could be pair, two-pairs, three, four,
    yacht, full-house, small-straight, big-straight or none,
    separated with spaces. It's a kind of game based on the rules of the
    Poker called Dice's Poker.
    :param l1:
    :return:
    """
    vals = ['pair', 'three', 'four', 'yacht', 'two-pairs', 'full-house', 'small-straight', 'big-straight']
    result, n, results, cont, conts, chave, chaves = [], 0, [], [], [], [], []
    for i in range(0, len(l1)):
        val = dict(Counter(l1[i]))
        results.append(val)
    print(results)
    for i in range(0, len(results)):
        for keys, values in results[i].items():
            cont.append(values)
            chave.append(keys)
        conts.append(cont)
        chaves.append(chave)
        cont = []
        chave = []
    for i in range(0, len(chaves)):
        print(chaves[i])
        if conts[i].count(2) == 1 and conts[i].count(1) == 3:
            cont.append(vals[0])
        elif conts[i].count(3) == 1 and conts[i].count(1) == 2:
            cont.append(vals[1])
        elif conts[i].count(4) == 1 and conts[i].count(1) == 1:
            cont.append(vals[2])
        elif conts[i].count(5) == 1:
            cont.append(vals[3])
        elif conts[i].count(2) == 2 and conts[i].count(1) == 1:
            cont.append(vals[4])
        elif conts[i].count(3) == 1 and conts[i].count(2) == 1:
            cont.append(vals[5])
        elif conts[i].count(1) == 5 and 6 not in chaves[i]:
            cont.append(vals[6])
        elif conts[i].count(1) == 5 and 1 not in chaves[i]:
            cont.append(vals[7])
    print(*cont)


yachtGame(strinToInteger())
