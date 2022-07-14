print('')


def two_printers():
    lista = [1, 1, 745849680]
    tempos, n, tempo_total = [], 1_000, 0
    for i in range(0, len(lista), 3):
        cont, page0, page1, p1, p2 = 0, 0, 0, 1, 1
        a = lista[i + 2] // 1_000

        b = lista[i + 2] % 1_000
        while page0 + page1 < (a * 1000):
            if cont == lista[i] * p1:
                page1 += 1
                p1 += 1
            if cont == lista[i + 1] * p2:
                page0 += 1
                p2 += 1
            if page0 + page1 >= (a * 1000):
                tempo_total += cont
                break
            cont += 1
        cont, page0, page1, p1, p2 = 0, 0, 0, 1, 1
        while page0 + page1 < b:
            if cont == lista[i] * p1:
                page1 += 1
                p1 += 1
            if cont == lista[i + 1] * p2:
                page0 += 1
                p2 += 1
            if page0 + page1 >= b:
                tempo_total += cont
                break
            cont += 1
        tempos.append(tempo_total)
    print(*tempos)


two_printers()

# 372924804
