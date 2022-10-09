from csv import reader


def deck():
    """
    This function take two list, one with suits, and the other one with
    the rank of a deck of cards and return the deck it in the traditional
    position.
    :return:
    """
    suits = ["C", "D", "H", "S"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    l1 = []
    for i in range(0, len(suits)):
        for k in range(0, len(ranks)):
            card = suits[i] + ranks[k]
            l1.append(card)
    return l1


def cardsShuffling(l1):
    """
    This function open a .csv sequence of non-negative integer random numbers,
    if they are greater than necessary, trim them to required range by taking
    modulo 52 and return the shuffling printing the new order of cards.
    :return:
    """
    arq = open("problem045.csv")
    l2 = reader(arq, delimiter=" ")
    l2 = list(*l2)
    print(l2)
    for i in range(0, len(l2)):
        swap = int(l2[i]) % 52
        l1[i], l1[swap] = l1[swap], l1[i]
    return print(*l1)


cardsShuffling(deck())
