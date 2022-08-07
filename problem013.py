from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return the values in a list
    from a string to a integer number.
    :return:
    """
    arq = open("problem013.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
    return l2


def splittingToDecimal(l2):
    """
    This function splitting values to decimal digits.
    :return:
    """
    l3, l4 = [], []
    for i in range(0, len(l2)):
        while l2[i] > 0:
            divrest = l2[i] % 10
            l3.append(divrest)
            l2[i] //= 10
        l3.reverse()
        l4.append(l3)
        l3 = []
    return l4


def weightedSumOfDigits(l4):
    """
    This function calculate the sum of digits, but multiplying 
    each digit given in a list from the above function for its 
    position (counting from the left, starting from 1).
    :return:
    """
    soma, somas, n = 0, [], 1
    for i in range(0, len(l4)):
        for k in range(0, len(l4[i])):
            soma += l4[i][k] * n
            n += 1
        somas.append(soma)
        soma = 0
        n = 1
    return print(*somas)


weightedSumOfDigits(splittingToDecimal(stringToInteger()))
