from csv import reader


def cardsOfTheDeck():
    """
    This function return the cards of a deck without count the suits.
    :return:
    """
    l1 = []
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for i in range(0, len(deck)):
        l1.append(deck[i])
    return l1


def valuesOfTheCards():
    """
    This function return the values of the cards of a deck under the 
    rules of Blackjack's game.
    :return:    
    """
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    l2 = []
    for i in range(0, len(deck)):
        if deck[i] in "123456789":
            l2.append(int(deck[i]))
        elif deck[i] in "TJQK":
            l2.append(10)
        elif deck[i] in "A":
            l2.append(11)
    return l2


def cardsInAList():
    """
    This function open a .csv file and return a list with
    the cards given.
    :return:
    """
    arq = open("problem042.csv")
    l3 = reader(arq, delimiter=" ")
    l3 = list(l3)
    return l3


def blackjackCounting(l1, l2, l3):
    """
    This function take the parameters given by the functions
    above and return the result of the game Blackjack, been
    the respecting the rules of the game.
    :param l1:
    :param l2:
    :param l3
    :return:
    """
    cont1, cont2, l4, n, m = 0, 0, [], 0, 0
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            #  In this snippet of the code the loop is divided
            #  in two paths. if there is the ace in the cards received
            # or not.
            if "A" in l3[i]:
                # In this snippet is count the number of aces in the
                # cards received.
                n = l3[i].count("A")
                if l3[i][k] == "A":
                    cont1 += l2[-1]
                elif l3[i][k] != "A":
                    cont1 += l2[l1.index(l3[i][k])]
                # In this snippet, following the rules of the Blackjack's game
                # two values can be received the ace cards, 1 or 11.
                # The chose should be the one whose result is the best, ie
                # closer or equal to 21.
                while cont1 > 21:
                    cont1 -= 10
                    m += 1
                    if m > n:
                        cont1 += 10
                        break
            elif "A" not in l3[i]:
                cont2 += l2[l1.index(l3[i][k])]
        # In this snippet is counted the points of the cards in the
        # hand of the player, following the rules of Blackjack game.
        if cont2 == 0:
            if cont1 <= 21:
                l4.append(cont1)
            else:
                l4.append("Bust")
        if cont1 == 0:
            if cont2 <= 21:
                l4.append(cont2)
            else:
                l4.append("Bust")
        cont1 = 0
        cont2 = 0
        m = 0
    return print(*l4)


blackjackCounting(cardsOfTheDeck(), valuesOfTheCards(), cardsInAList())

# 18 21 18 19 16 17 19 21 16 16 21 21 21 16 21 19 16 Bust 20 Bust
