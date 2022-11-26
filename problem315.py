from csv import reader


def stringToInteger():
    """
    This function open a cvs file and return a list of integer.
    :return:
    """
    arq = open("problem315.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    print(l1)
    return l1


def countTheCommonFactors(l1):
    """
    This function take a parameter given by the function above and
    returns for each pair of numbers all common factors produced by
    iterating of the data.
    :param l1:
    :return:
    """
    n, set1, set2, set3, cont, l2 = 0, {(), 1}, {(), 1}, {()}, 0, []
    set1.discard(())
    set2.discard(())
    set3.discard(())
    while n < 8:
        for i in range(0, len(l1)):
            for k in range(0, len(l1[i])):
                a = l1[i][k]
                c = a
                c = c + 1
                print(c)
                for m in range(2, 100_000):
                    while c % m == 0 and m != c:
                        c /= m
                        set1.add(k)
        n += 1
    n = 0
    while n < 8:
        for i in range(0, len(l1)):
            for k in range(0, len(l1[i])):
                b = l1[i][k]
                d = b
                d += 1
                for m in range(2, 100_000):
                    while d % m == 0 and m != d:
                        d /= m
                        set2.add(m)
        n += 1
        set3 = set1.intersection(set2)
        cont = len(set3)
        l2.append(cont)
    return print(*l2)


countTheCommonFactors(stringToInteger())
