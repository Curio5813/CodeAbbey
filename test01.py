

def anagrams():

    palavra, words, anagrama, anagramas, n, cont, encontradas = '', [], {()}, [], 0, 0, []
    with open('words.txt') as arquivo:
        lista = list(arquivo)
    for k in range(0, len(lista)):
        palavra += lista[k]
        palavra = palavra.replace('\n', '')
        words.append(palavra)
        palavra = ''
    palavra = ['ingress', 'reveres', 'parties', 'reaps', 'setters', 'derange', 'rapiers', 'predator']
    for k in range(0, len(palavra)):
        anagrama.update(''.join(x) for x in permutations(palavra[k]))
        anagrama.discard(palavra[k])
        anagramas.append(list(anagrama))
        anagrama = set()
    for k in range(0, len(anagramas)):
        while n < len(anagramas[k]):
            if anagramas[k][n] in words:
                cont += 1
            n += 1
        encontradas.append(cont)
        cont = 0
        n = 0
    print(*encontradas)


anagrams()







