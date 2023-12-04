from csv import reader
import numpy as np


def simple_linear_regression():
    """
    Brethren of CodeAbbey are running several small businesses to support
    the Monastery. One of them is the Winemaking.

    One of the interesting issues here is that the price of the wine is not
    constant. At some years customers are ready to buy more barrels and pay
    higher, while at other years they are reluctant and brotherhood needs to
    lower prices to get rid of wine stores.

    It was found that the reason for such behavior is simple - after rainy
    years grapes yield wine of better quality and people are more eager to
    purchase it.

    This gives monks the idea - they need to find the formula for calculating
    more just price depending on weather records from the preceeding year, so
    that trade will run more smoothly. (the wine which is sold this year was
    prepared from the grapes picked the year before)

    You are to help them in finding this formula. To keep things simple let us
    try approximating the dependency with the linear function in the form

    Y = K * X + B
    Where X is the amount of rainy days and Y is the price.

    Problem statement
    You will be given a list of records, each containing the number of rainy days
    during previous year along with the average price for which the wine was sold
    during current year.

    Use the Simple Linear Regression and criteria of the Ordinary Least Squares to
    find parameters of the linear function which can approximate the dependence
    between price and amound of rainy days.

    Input data contains starting A and ending B year in the first line.
    Then lines follow for each year in form YYYY: D P where YYYY is the mark of year,
    D is the number of rainy days (in previous season) and P is the wine price (in
    crowns per barrel).
    Answer should contain values for K and B with accuracy of 1e-7 or better.
    :return:
    """
    arq = open("problem095.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3, l4, l5, reta = [], [], [], [], 0
    for i in range(0, len(l1)):
        for k in range(1, len(l1[i])):
            l2.append(float(l1[i][1]))
            l3.append(float(l1[i][2]))
            break
        l4.append(*l2)
        l5.append(*l3)
        l2 = []
        l3 = []
    x = np.array(l4)
    y = np.array(l5)
    a = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(a, y, rcond=None)[0]
    print(m, c)


simple_linear_regression()
