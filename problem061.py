from csv import reader


def stringToInteger():
    """
    This function open a .csv file and return a list of integer.
    :return:
    """
    arq = open("problem061.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def primeNumbersGeneration(l1):
    """
    This function take the parameter given the function above
    and return a list of prime numbers with the index is given by
    the list above.
    :param l1
    :return:
    """
    l2 = []
    prime, not_prime = [], set()
    for n in range(2, 3_000_000):
        if n in not_prime:
            continue
        for f in range(n * 2, 3_000_000, n):
            not_prime.add(f)
        prime.append(n)
    for i in l1:
        l2.append(prime[i - 1])
    return print(*l2)


primeNumbersGeneration(stringToInteger())
