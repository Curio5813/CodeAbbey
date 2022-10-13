from itertools import permutations
from csv import reader


def dictIntoArray():
    """
    This function open a .csv file and return a list of english
    words in dictionary.
    :return:
    """
    arq = open("problem127-dict.csv")
    l1 = reader(arq, delimiter="\n")
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(l1[i][k])
    return l2


def strinstIntoArray():
    """
    This function open a .csv file and return a list of english
    words.
    :return:
    """
    arq = open("problem127-data.csv")
    l3 = reader(arq, delimiter="\n")
    l3 = list(l3)
    l4 = []
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            l4.append(l3[i][k])
    return l4


def anagrams(l2, l4):
    """
    This function receive a list of english words as one
    parameter and also the words in the english's dictionary
    as another parameter and return the number the all words in
    a anagrams is in the english dictionary (not including
    the word itself).
    :param l2
    :param l4:
    :return:
    """
    word, per, l5, l6, l7, cont = "", [], [], [], [], -1
    for i in range(0, len(l4)):
        # Permutation words using Intertools Library
        # pushed to a array per.
        per.append((list(permutations(l4[i]))))
    for i in range(0, len(per)):
        for k in range(0, len(per[i])):
            for m in range(0, len(per[i][k])):
                # Concatenating strings to form a word.
                word += per[i][k][m]
            if word not in l5:
                # Eliminate word in duplicity.
                l5.append(word)
            word = ""
        l6.append(l5)
        l5 = []
    for i in range(0, len(l6)):
        for k in range(0, len(l6[i])):
            # In this snippet of the code puts in a list the words
            # that have in the English dictionary using the anagrams
            # formed with the given words.
            if l6[i][k] in l2:
                cont += 1
        l7.append(cont)
        cont = -1
    return print(*l7)


anagrams(dictIntoArray(), strinstIntoArray())
