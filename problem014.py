from csv import reader


def stringToSignal():
    """
    This function take a .csv file and convert it to signal
    arithmetic operations.
    :return:
    """
    arq = open("problem014.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2 = ["="]  # I put the list not empty to avoid list index error
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if i > 0:
                l2.append(l1[i][0])
                break
    return l2


def stringToInterger():
    """
    This function extracts integer numbers from a .csv file as string
    and converts them to integers.
    :return:
    """
    arq = open("problem014.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l3 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if i == 0:
                l3.append(int(l1[i][0]))
                break
            elif i > 0:
                l3.append(int(l1[i][1]))
                break
    return l3


def modularCalculator(l2, l3):
    """
    This function have a kind of long arithmetic calculation, take from a list
    in the above function, and return the modulo of the arithmetic operations
    given.
    :return:
    """
    sumult = 0
    for i in range(0, len(l2)):
        if l2[i] == "=":
            sumult += l3[i]
        elif l2[i] == "+":
            sumult += l3[i]
        elif l2[i] == "*":
            sumult *= l3[i]
        elif l2[i] == "%":
            return print(sumult % l3[i])


modularCalculator(stringToSignal(), stringToInterger())
