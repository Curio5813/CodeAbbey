"""
========
Anagrams
========

The idea proposed by Guy Gervais was so fruitful that it allows to create more than one problem from it.
Here is the simpler one.

In many natural languages we can find some pairs of words which could be transformed to each other by
changing the order of letters. I.e. they consist of the same set of letters, for example:

cat - act take - teak ate - eat - tea

Such words are called anagrams and as we see in the third example sometimes there are more than two words.

Your task is to find out the amount of anagrams for given word by the dictionary.

Click this link with right mouse button and select "Save As" to download dictionary file

Dictionary file contains a list of english words, one per line. It was taken from Ubuntu linux distribution
and stripped of words containing capital letters, apostrophes and non-english letters.

Input data will contain the number of test-cases in the first line.
Next lines will contain a single word each.
Answer should contain the number of anagrams for each word (not including the word itself).

Example:

input data:
3
bat
coal
lots

answer:
1 1 2
"""
print('')


def anagrams():
    from itertools import permutations
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
