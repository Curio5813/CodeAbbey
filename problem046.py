from csv import reader


def stringToInteger():
    """
    This function open a csv. file and return a list of integer.
    :return:
    """
    arq = open("problem046.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    print(l1)
    return l1


def ticTacToe(l1):
    """
    The function take the parameter given for the function above
    and return should contain the number of the move at which game
    the tic-tac-toe is won by one of players (starting from 1) or 0
    if the game is drawn (no winner) after the last move.
    :param l1:
    :return:
    """
    j, js, p1, p2, res = [], [], [], [], []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            j.append(l1[i][k])
        js.append(j)
        j = []
    for i in range(0, len(js)):
        for k in range(0, len(js[i])):
            if k % 2 == 0:
                p1.append(js[i][k])
            if 1 in p1 and 2 in p1 and 3 in p1:
                res.append(k + 1)
                break
            elif 4 in p1 and 5 in p1 and 6 in p1:
                res.append(k + 1)
                break
            elif 7 in p1 and 8 in p1 and 9 in p1:
                res.append(k + 1)
                break
            elif 1 in p1 and 4 in p1 and 7 in p1:
                res.append(k + 1)
                break
            elif 2 in p1 and 5 in p1 and 8 in p1:
                res.append(k + 1)
                break
            elif 3 in p1 and 6 in p1 and 9 in p1:
                res.append(k + 1)
                break
            elif 1 in p1 and 5 in p1 and 9 in p1:
                res.append(k + 1)
                break
            elif 3 in p1 and 5 in p1 and 7 in p1:
                res.append(k + 1)
                break
            if k % 2 == 1:
                p2.append(js[i][k])
            if 1 in p2 and 2 in p2 and 3 in p2:
                res.append(k + 1)
                break
            elif 4 in p2 and 5 in p2 and 6 in p2:
                res.append(k + 1)
                break
            elif 7 in p2 and 8 in p2 and 9 in p2:
                res.append(k + 1)
                break
            elif 1 in p2 and 4 in p2 and 7 in p2:
                res.append(k + 1)
                break
            elif 2 in p2 and 5 in p2 and 8 in p2:
                res.append(k + 1)
                break
            elif 3 in p2 and 6 in p2 and 9 in p2:
                res.append(k + 1)
                break
            elif 1 in p2 and 5 in p2 and 9 in p2:
                res.append(k + 1)
                break
            elif 3 in p2 and 5 in p2 and 7 in p2:
                res.append(k + 1)
                break
            if k >= len(js[i]) - 1:
                res.append(0)
                break
        p1, p2 = [], []
    return print(*res)


ticTacToe(stringToInteger())
