from csv import reader


def linearFunction():
    """
    This function returns the values of constants "a" and "b", given
    the pairs "x" and "y" values found in a liner function.
    :return:
    """
    arq = open("problem010.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3, a, b, l4, l5 = [], [], 0, 0, [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(int(l1[i][k]))
        l3.append(l2)
        l2 = []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            x1 = l3[i][0]
            y1 = l3[i][1]
            x2 = l3[i][2]
            y2 = l3[i][3]
            if x1 > 0 and x2 > 0 and a >= 0 and a * x1 * x2 - a * x2 * x1 == 0:
                b = (y1 * x2) / x2
                a = (y1 - b) / x1
                l4.append(a)
                l4.append(b)
                break
            elif x1 == 0 or x2 == 0:
                b = y1
                l4.append(b)
                break
        l5.append(l4)
        l4 = []
    print(l5)


linearFunction()
