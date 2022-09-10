from csv import reader


def stringToInteger():
    """
    This function open .csv and return a list of integer
    :return:
    """
    arq = open("problem044.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    return l3


def doubleDiceRoll(l3):
    """
    This function takes from function above as parameter the lists and
    return the numbers from 2 dices throw. it happens that
    this case is even simpler. We can use the following approach:
    Divide the random value R by the N (number of distinct values
    we want - e.g. 6 for dice) and take the remainder. This
    remainder is necessarily the integer value in the range from 0 to N - 1.
    Now to shift it to the necessary range, simply add 1 (i.e. the minimum
    of the range we want) - and you'll get the value in the range from 1 to N.
    This method is not well precise if N is not small enough in compare
    to max of the generator. However, it will be all right for most everyday
    needs (tossing coins, rolling dice, shuffling cards etc.)
    :param l3
    :return:
    """
    soma, l4 = 0, []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            d1 = (l3[i][0] % 6) + 1
            d2 = (l3[i][1] % 6) + 1
            soma = d1 + d2
            l4.append(soma)
            break
    return print(*l4)


doubleDiceRoll(stringToInteger())
