def main():
    from csv import reader
    """
    Minimum of Two: Of two numbers, please, select one with minimum value. Here are several pairs of
    numbers for thorough testing. Input data will contain number of test-cases in the first line.
    Following lines will contain a pair of numbers to compare each.
    For Answer please enter the same amount of minimums separated by space, for example:

    data:
    3
    5 3
    2 8
    100 15

    answer:
    3 2 15
    """
    lista1, lista2, minimum = [], [], []
    with open('minimum_of_two.csv') as arquivo:
        leitor_csv = reader(arquivo, delimiter=' ')
        lista = [linha for linha in leitor_csv]
    for k in range(0, len(lista)):
        for i in range(0, len(lista[k])):
            lista1.append(int(lista[k][i]))
        lista2.append(lista1)
        minimum.append(min(lista2[k]))
        lista1 = []
    print(*minimum)


if __name__ == '__main__':
    main()
