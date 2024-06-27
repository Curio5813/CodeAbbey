from csv import reader


def insertion_sort():
    """
    This functions how much elements had shifted at ecah pass
    using insertion sort.
    :return:
    """
    arq = open("problem121.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, cont, trocados = [], 0, []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(int(l1[i][k]))
        break
    for i in range(1, len(l2)):
        compara = l2[i]
        j = i - 1
        while j >= 0 and l2[j] > compara:
            l2[j + 1] = l2[j]
            j -= 1
            cont += 1
        trocados.append(cont)
        cont = 0
        l2[j + 1] = compara

    print(*trocados)


insertion_sort()
