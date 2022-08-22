from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of integers and float.
    :return:
    """
    l2, l3 = [], []
    arq = open("problem028.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][0] = int(l1[i][0])
            l1[i][1] = float(l1[i][1])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    return l3


def bodyMassIndex(l3):
    """
    This function takes a list as parameter given by the function
    above and print a list of body mass index situation.
    :param l3:
    :return:
    """
    l4 = []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            bmi = l3[i][0] / (l3[i][1] ** 2)
            if bmi < 18.5:
                situation = 'under'
                l4.append(situation)
                break
            if 18.5 <= bmi < 25:
                situation = 'normal'
                l4.append(situation)
                break
            if 25.5 <= bmi < 30:
                situation = 'over'
                l4.append(situation)
                break
            if 30 <= bmi:
                situation = 'obese'
                l4.append(situation)
                break
    for i in range(0, len(l4)):
        print(l4[i], end=" ")


bodyMassIndex(stringToInteger())
