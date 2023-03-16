from csv import reader
from math import floor


def stringToInteger():
    """
    This function open a csv file and return a list of integer.
    :return:
    """
    arq = open("problem080.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = float(l1[i][k])
    return l1


def duelChances(l1):
    """
    This function get the probability for both duellers to
    hit and hurt opponent critically with a single shot, given by
    the function above and returns the Alan's chances to win the duel
    based in the conditional probabilities of each dueller, that
    means Bob's chances to win could be calculated as Alan's chances
    to die.
    :param l1:
    :return:
    """
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            pa = l1[i][0] / 100
            pac = 1 - pa
            pb = l1[i][1] / 100
            pbc = 1 - pb
            # Formula to calculate the conditional probabilities.
            formula = (pa / (1 - pac * pbc)) * 100
            # Adding 0.5 to take de nearst integer get from the formula gave above.
            formula += 0.5
            # The floor method rounds to the nearest integer below the float number.
            l2.append(floor(formula))
            break
    return print(*l2)


duelChances(stringToInteger())
