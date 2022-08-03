from csv import reader


def rounding():
    """
    This function returns the value closest to one of the given fraction
    in a list with two values, the first being the dividend, and the second
    being the divisor.
    :return:
    """
    arq = open("problem006.csv")
    lr = reader(arq, delimiter=" ")
    lr = list(lr)
    d1, d2, r = [], [], []
    for i in range(0, len(lr)):
        for k in range(0, len(lr[i])):
            d1.append(int(lr[i][k]))
        d2.append(d1)
        d1 = []
    for i in range(0, len(d2)):
        for k in range(0, len(d2[i])):
            dfra = d2[i][0] / d2[i][1]
            dint = d2[i][0] // d2[i][1]
            if dfra < 0 and dfra - dint == -0.5:  # To take closest integer up
                rond = dint + 1                   # for negative numbers.
                r.append(rond)
                break
            elif dfra > 0 and dfra - dint == 0.5:  # To take closest integer up.
                rond = dint + 1                    # # for positive numbers.
                r.append(rond)
                break
            else:
                r.append(round(dfra))
                break
    return print(*r)


rounding()
