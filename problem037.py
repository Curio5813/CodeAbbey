from csv import reader


def stringToInteger():
    """
    This function open a .csv file a return a list of integer.
    :return:
    """
    arq = open("problem037.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def mortgageCalculator(l1):
    """
    This function receives three value, the value of the loan,
    the rate and the term to pay all debits and return the
    value of parcels rounded to the first integer above.
    :return:
    :param l1:
    :return:
    """
    loan, r, term, month = 0, 0, 0, 0
    for i in range(0, len(l1)):
        loan, r, term = l1[i], l1[i + 1], l1[i + 2]
        break
    r = (r / 12) / 100
    parcel = round(loan / term)
    while loan > 0:
        loan += loan * r
        loan -= parcel
        loan = round(loan)
        month += 1
        if month == term and loan > 0:
            parcel += 1
            loan = l1[0]
            month = 0
    return print(round(parcel))


mortgageCalculator(stringToInteger())
