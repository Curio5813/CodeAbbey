from csv import reader


def sumsInLoop():
    """
    This funtion calculate the sum of pairs in a nested list from a
    given list.
    :return:
    """
    arq = open("problem003.csv")
    lp = reader(arq, delimiter=" ")
    lp = list(lp)
    soma, somas = 0, []
    for i in range(0, len(lp)):
        for k in range(0, len(lp[i])):
            soma += int(lp[i][k])
        somas.append(soma)
        soma = 0
    return print(*somas)


sumsInLoop()
