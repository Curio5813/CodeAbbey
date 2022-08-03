from csv import reader


def fahrenheitToCelsius():
    """
    This function convert Fahrenheit to Celsius to measuring
    the temperature in this scale.
    :return:
    """
    arq = open("problem007.csv")
    lf = reader(arq, delimiter=" ")
    lf = list(lf)
    lf2, lc = [], []
    for i in range(0, len(lf)):
        for k in range(0, len(lf[i])):
            lf2.append(int(lf[i][k]))
    for i in lf2:
        c = (i - 32) / 1.8  # This is the formula to convert Fahrenheit to Celsius.
        lc.append(round(c))
    return print(*lc)


fahrenheitToCelsius()
