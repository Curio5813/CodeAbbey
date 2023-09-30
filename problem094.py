from csv import reader


def fool_day_2014():
    """
    This function calculate a sequence of numbers that
    form a patterns.
    :return:
    """
    arq = open("problem094.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, soma = [], 0
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            soma += l1[i][k] * l1[i][k]
        l2.append(soma)
        soma = 0
    print(*l2)


fool_day_2014()
