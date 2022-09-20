from csv import reader


def stringForSortedDeck():
    """
    This function open a .cvs file and gives an integer, the number
    of the card sorted in full deck.
    :return:
    """
    arq = open("problem058.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    return l1


def cardNames(l1):
    """
    This function receives the parameter given by the function
    above and return a list with the name of some the cards in
    the full deck.
    :param l1
    :return
    """
    suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    rk = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card, name_cards, cards = [], '', []
    for i in range(0, len(l1)):
        suit = l1[i] // 13
        rank = l1[i] % 13
        name_cards = rk[rank] + "-" + "of" + "-" + suits[suit]
        cards.append(name_cards)
    return print(*cards)


cardNames(stringForSortedDeck())
