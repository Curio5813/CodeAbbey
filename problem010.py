from csv import reader


def linearFunction():
    """
    This function returns the values of constants "a" and "b", given
    the pairs "x" and "y" of the cartesian values found in linear
    function.
    :return:
    """
    arq = open("problem010.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3, a, b, l4, n = [], [], 0, 0, [], 0
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
            dx = x2 - x1
            dy = y2 - y1
            if dx != 0:
                a = dy / dx  # This caculate the angular coeficient of the 1º function.
                b = (y1 * x2 - y2 * x1) / (x2 - x1)  # This calculate the constant term.
                l4.append(int(a))
                l4.append(int(b))
                break
    for i in range(0, len(l4), 2):
        print(f"({l4[i]} {l4[i + 1]})", end=" ")


linearFunction()
