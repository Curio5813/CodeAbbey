from csv import reader


def code_guesser():
    """
    This function open a .csv file and return a list of nested string.
    :return:
    """
    arq = open("problem036.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    (digito, digitos, errados, talvez1, talvez2, temp, certo, talvez3, n, duvida, idx, flag, idx3) = (
        [], [], [], [], [], [], ['x', 'x', 'x', 'x'], ['s', 's', 's', 's'],
        0, ['n', 'n', 'n', 'n'], [], 0, 0)
    for i in range(0, len(l1)):
        for j in range(0, len(l1[i])):
            for k in range(0, len(l1[i][j])):
                digito.append(int(l1[i][j][k]))
        digitos.append(digito)
        digito = []
    # print(digitos)
    for i in range(0, len(digitos)):
        for j in range(0, len(digitos[i])):
            if j == 4:
                break
            if digitos[i][-1] == 0:
                temp.append(digitos[i][j])
        if len(temp) > 0:
            errados.append(temp)
        temp = []
    for i in range(0, len(digitos)):
        for j in range(0, len(digitos[i])):
            if j == 4:
                break
            if digitos[i][-1] == 1:
                temp.append(digitos[i][j])
        if len(temp) > 0:
            talvez1.append(temp)
        temp = []
    for i in range(0, len(digitos)):
        for j in range(0, len(digitos[i])):
            if j == 4:
                break
            if digitos[i][-1] == 2:
                temp.append(digitos[i][j])
        if len(temp) > 0:
            talvez2.append(temp)
        temp = []
    for i in range(0, len(errados)):
        for k in range(0, len(errados[i])):
            if errados[i][k] == talvez2[n][k]:
                talvez3.insert(k, 'n')
                talvez3.pop(k + 1)
        n += 1
        if n >= len(talvez2) - 1:
            n = 0
    n = 0
    for i in range(0, len(talvez3)):
        if talvez3[i] == "s":
            certo.insert(i, talvez2[0][n])
            idx.append(i)
            certo.pop(i + 1)
        n += 1
        if n >= 4:
            break
    print(certo)
    print(idx)
    n = 0
    for i in range(0, len(certo)):
        if certo[i] != "x":
            duvida.insert(i, certo[i])
            duvida.pop(i + 1)
        if certo[i] == "x":
            for j in range(0, len(errados)):
                for k in range(0, len(errados[j])):
                    if ((k == i and talvez1[n][idx[0]] != certo[idx[0]]
                            and talvez1[n][idx[1]] != certo[idx[1]]) and talvez1[n][k]
                            not in duvida):
                        flag = 1
                        idx3 = k

                if flag == 1:
                    duvida.insert(idx3, talvez1[n][idx3])
                    duvida.pop(idx3 + 1)
                    flag = 0
                    print(duvida)
                n += 1
                if n >= len(talvez1) - 1:
                    n = 0

    print(errados)
    print(talvez1)
    print(duvida)


code_guesser()
