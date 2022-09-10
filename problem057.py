from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of float numbers.
    :return:
    """
    arq = open("problem057.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = float(l1[i])
    return l1


def smoothingTheWeather(l1):
    """
    This function take a list with float numbers from the function above
    as a parameter and return a print of the float numbers whom make a
    measuring more approximate from the real temperature.
    :param l1:
    :return:
    """
    l2 = [l1[0]]
    for i in range(0, len(l1)):
        if i >= len(l1) - 2:
            l2.append(l1[-1])
            break
        soma = l1[i] + (l1[i + 1]) + (l1[i + 2])
        media = round((soma / 3), 8)
        l2.append(media)
    return print(*l2)


smoothingTheWeather(stringToInteger())
