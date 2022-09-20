from csv import reader


def stringToList():
    """
    This function open a .cvs file and return a list of strings
    formatted.
    :return:
    """
    arq = open("problem049.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    return l1


def rockPaperScissors(l1):
    """
    This function is about a game which is of special importance in the Computer
    Science because it though simple itself, could be used for creating
    very cunning Artificial Intelligence algorithms to play against
    human (or each other) with predicting the opponent's behavior.
    This ancient game is played between two participants who simultaneously
    cast one of three figures by their fingers - Rock, Paper or Scissors.
    If both cast the same figure, the round is considered a draw, otherwise,
    the following rules are applied. The function receive a parameter, a list,
    with several records of the played games. The return give the result of
    which player won, if the first or the second, in each match.
    :param l1:
    :return:
    """
    print(l1)
    p1, p2, l2, l3, l4 = 0, 0, [], [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if l1[i][k] == 'PR':
                l2.append(1)
            elif l1[i][k] == 'RS':
                l2.append(1)
            elif l1[i][k] == 'SP':
                l2.append(1)
            elif l1[i][k] == 'RP':
                l2.append(2)
            elif l1[i][k] == 'SR':
                l2.append(2)
            elif l1[i][k] == 'PS':
                l2.append(2)
        if l2.count(1) > l2.count(2):
            l3.append(1)
        elif l2.count(1) < l2.count(2):
            l3.append(2)
        l2 = []
    return print(*l3)


rockPaperScissors(stringToList())
