from csv import reader
from math import sqrt


def stringToInteger():
    """
    This function open a .csv file and returns a list of
    integer.
    :return:
    """
    arq = open("problem104.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    print(l3)
    return l3


def sidesOfTheTriangle(l3):
    """
    This function takes the list given from the function above
    as a parameter and return a list of the sides of the triangles.
    :param l3:
    :return:
    """
    l4, l5 = [], []
    # This loop takes the coordinates given and find the points
    # to construct a triangle by distance from your points.
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            x1 = l3[i][k]
            y1 = l3[i][k + 1]
            x2 = l3[i][k + 2]
            y2 = l3[i][k + 3]
            x3 = l3[i][k + 4]
            y3 = l3[i][k + 5]
            a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            b = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
            c = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
            l4.append(a)
            l4.append(b)
            l4.append(c)
            break
        l5.append(l4)
        l4 = []
    return l5


def areaOfTheTriangles(l5):
    """
    This function takes the parameter given to the function above
    with the sides of triangles and returns the area for each triangle
    using the Heron's formula.
    :param l5:
    :return:
    """
    print(l5)
    l6 = []
    for i in range(0, len(l5)):
        for k in range(0, len(l5[i])):
            # Below is using the Heron's formula.
            # It is equal the semi-perimeter of the triangles.
            s = (l5[i][0] + l5[i][1] + l5[i][2]) / 2
            a = sqrt(s * (s - l5[i][0]) * (s - l5[i][1]) * (s - l5[i][2]))
            l6.append(a)
            break
    return print(*l6)


areaOfTheTriangles(sidesOfTheTriangle(stringToInteger()))
