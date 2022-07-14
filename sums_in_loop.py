def main():
    from csv import reader
    """
    Sums in Loop
    """
    lista1, lista2, somas = [], [], []
    with open('sums_in_loop.csv') as arquivo:
        leitor_csv = reader(arquivo, delimiter=' ')
        lista = [linha for linha in leitor_csv]
    for k in range(0, len(lista)):
        for i in range(0, len(lista[k])):
            lista1.append(int(lista[k][i]))
        lista2.append(lista1)
        somas.append(sum(lista2[k]))
        lista1 = []
    print(*somas)


if __name__ == '__main__':
    main()
