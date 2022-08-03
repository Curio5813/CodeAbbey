from csv import reader


def minimumOfThree():
    """
    This function give smallest number between three numbers given in a list.
    :return:
    """
    arq = open("problem005.csv")
    mt = reader(arq, delimiter=" ")
    mt = list(mt)
    min1, min2 = [], []
    for i in range(0, len(mt)):
        for k in range(0, len(mt[i])):
            min1.append(int(mt[i][k]))
        min2.append(min(min1))
        min1 = []
    return print(*min2)


minimumOfThree()
