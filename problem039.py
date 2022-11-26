from statistics import stdev, mean


def sharePriceVolatile():
    texto, dados, n, share, dado, prices, choice = '', [], 0, [], [], [], []
    with open('problem039.txt') as arquivo:
        lista = list(arquivo)
    for k in range(0, len(lista)):
        texto += lista[k]
        texto = texto.replace('\n', '')
        dados.append(texto.split(' '))
        texto = ''
    for k in range(0, len(dados)):
        while n <= len(dados[k]):
            if n == 0:
                share.append(dados[k][n])
            if n > 0:
                dados[k][n] = int(dados[k][n])
                dado.append(dados[k][n])
            n += 1
            if n == len(dados[k]):
                break
        prices.append(dado)
        n = 0
        dado = []
    for k in range(0, len(prices)):
        media = mean(prices[k])
        desv_padrao = stdev(prices[k])
        tax = media * 0.01
        if desv_padrao >= 4 * tax:
            choice.append(share[k])
    print(*choice)


sharePriceVolatile()
