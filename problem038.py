from csv import reader
from math import sqrt


def stringToInteger():
    """
    This function open a .csv file and returns a list o integer.
    :return:
    """
    arq = open("problem038.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3 = [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    return l3


def quadraticEquation(l3):
    """
    This function receive a nested list of integer and given
    as parameter return a list the roots even the roots not being parts
    the real numbers' domain

       ax² + bx + c = 0  # General Formula for 2ª Equation

    :param l3:
    :return:
    """
    l4, l5 = [], []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            a = l3[i][0]
            b = l3[i][1]
            c = l3[i][2]
            delta = (b ** 2) - (4 * a * c)
            if delta > 0:
                x1 = (-b + sqrt(delta)) / (2 * a)
                x2 = (-b - sqrt(delta)) / (2 * a)
                if x1 >= x2:
                    l4.append(int(x1))
                    l4.append(int(x2))
                elif x1 < x2:
                    l4.append(int(x2))
                    l4.append(int(x1))
                break
            elif delta == 0:
                x1 = -b / (2 * a)
                x2 = x1
                l4.append(int(x1))
                l4.append(int(x2))
                break
            elif delta < 0:
                x1 = int(-b / (2 * a))
                x2 = int(-b / (2 * a))
                s = delta
                z1 = (sqrt(-s) / (2 * a))
                z2 = (-sqrt(-s) / (2 * a))
                y1 = complex(x1, int(z1))  # it's a built-in function to get complex number
                y2 = complex(x2, int(z2))  # the real part and the imaginary part, where i² = -1.
                if x1.real == 0:
                    l4.append(f"0+{y1}")
                    l4.append(f"0{y2}")
                else:
                    l4.append(y1)
                    l4.append(y2)
                break
        l5.append(l4)
        l4 = []
    return l5


def printRoots(l5):
    """
    This function take the parameter with a list o roots of second degree equation
    and has the return a print of each roots in the output formats wanted by the
    online judge.
    :param l5:
    :return:
    """
    for i in range(0, len(l5)):
        if i >= len(l5) - 1:
            print(f"{l5[i][0]} {l5[i][1]}".replace("j", "i").replace("(", "").replace(")", ""))
            break

        else:
            print(f"{l5[i][0]} {l5[i][1]};".replace("j", "i").replace("(", "").replace(")", ""), end=" ")


printRoots(quadraticEquation(stringToInteger()))
