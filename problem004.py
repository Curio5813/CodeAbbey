from csv import reader


def minimumOfTwo():
    """
    This function give the smallest number between two numbers given in a list.
    :return:
    """
    arq = open("problem004.csv")
    mt = reader(arq, delimiter=" ")
    mt = list(mt)
    min1, min2 = [], []
    for i in range(0, len(mt)):
        for k in range(0, len(mt[i])):
            min1.append(int(mt[i][k]))
        min2.append(min(min1))
        min1 = []
    return print(*min2)


minimumOfTwo()
