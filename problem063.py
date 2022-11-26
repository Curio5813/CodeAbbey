from csv import reader


def stringToInterger():
    """
    This function open a csv file and return a list of integers.
    :return:
    """
    arq = open("problem063.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
    return l2


def integerFactorization(l2):
    """
    This function takes the parameters given by the function above
    with a several integer numbers to decompose them into products
    of primes and return the product representation for each of
    these integers, written like p1*p2*p3 where p1 ... p3 are some
    primes sorted in non-decreasing order. Products should be separated
    with spaces.
    :param l2:
    :return:
    """
    n, fat, fats = 2, [], []
    for i in range(0, len(l2)):
        while l2[i] != 1:
            if l2[i] % n == 0:
                fat.append(n)
                l2[i] /= n
            else:
                n += 1
        fats.append(fat)
        fat = []
        n = 2
    for i in range(0, len(fats)):
        for k in range(0, len(fats[i])):
            if k >= len(fats[i]) - 1:
                print(f'{fats[i][k]}', end=' ')
                break
            print(f'{fats[i][k]}*', end='')


integerFactorization(stringToInterger())
