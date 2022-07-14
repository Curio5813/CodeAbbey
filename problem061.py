def gerar_primos():
    p, numeros, primos = [], [], []
    indices = []
    limite = 2000000 + 1
    nao_primo = set()
    for n in range(2, limite):
        if n in nao_primo:
            continue
        for f in range(n * 2, limite, n):
            nao_primo.add(f)
        primos.append(n)
    for k in range(0, len(indices)):
        numero = primos[indices[k] - 1]
        numeros.append(numero)
    print(*numeros)


gerar_primos()
