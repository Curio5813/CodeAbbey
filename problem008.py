from csv import reader


def arithmeticProgression():
    """
    This function calculate the sum of the frist Ns members of
    arithmetic progression given the first member, the ratio of
    the progression and the number of steps.
    :return:
    """
    arq = open("problem008.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3, soma, somas = [], [], 0, []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(int(l1[i][k]))
        l3.append(l2)
        l2 = []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            a = l3[i][0]
            q = l3[i][1]
            n = l3[i][2]
            an = a + (n - 1) * q  # This is the formula to calculate the last members.
            soma = (n * (a + an)) / 2  # This is the formula to calculate the sum of a P.A.
        somas.append(int(soma))
    print(*somas)


arithmeticProgression()
