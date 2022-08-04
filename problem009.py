from csv import reader


def triangles():
    """
    This function return 1 if it is possible to construct a triangle
    given the sizes of your sides, or 0 if it is impossible.
    :return:
    """
    arq = open("problem009.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            a, b, c = int(l1[i][0]), int(l1[i][1]), int(l1[i][2])
            if a + b > c and a + c > b and b + c > a:  # Inequality theorem of the sum
                l2.append(1)                           # of sides of a triangle.
                break
            else:
                l2.append(0)
                break
    print(len(l2))
    return print(*l2)


triangles()
