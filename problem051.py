from csv import reader
from math import floor, ceil
from statistics import mode, mean, median


def dungeons_and_dragons_dice():
    """
    In the complex dice-based games players can use several dice
    and with number of sides other than 6. For example, the damage
    given by some powerful sword could be calculated as the sum of
    3 dice with 8 sides each (i.e. having numbers from 1 to 8) -
    this means the weakest possible damage is 3 and strongest is 24,
    however most probable values would be 13 and 14.

    The notation used in the descriptions of such games looks like 3d8 - i.e.
    3 dice with 8 sides, or 2d6 for more common variant of 2 dice with 6
    sides each. Tossing of 5 coins each of which has only 2 sides would be
    written as 5d2.

    In this task you will be given results of casting some dice set many times.
    Your task would be to determine how many dice are in the set and how many
    sides dice have. Supposedly you'll need some program to calculate statistics
    on these results to classify them.

    Due to probabilistic nature of the problem you may fail at first attempt, however
    try a few times - and if your algorithm is correct, your answer will be accepted.

    For this problem dice could have 2, 4, 6, 8, 10 or 12 sides. The number of dice
    could be from 1 to 5.

    Input data contain 303 values in 3 lines.
    Each line contains 100 non-zero results of casting (sums of dice points), terminated
    with spare 0 which should not be counted (it only marks the end of the line).
    Answer should contain three description of dice sets for each of three lines, in form
    xdy where x and y are numbers of dice and of sides respectively.
    :return:
    """
    arq = open("problem051.csv")
    dados = reader(arq, delimiter=" ")
    dados = list(dados)
    dados_i, minimo, maximo, sides, dices, valrs, aux, trat, \
        resposta, respostas = [], 0, 0, 0, 0, [], [], [], "", []
    side = [2, 4, 6, 8, 10, 12]
    dice = [1, 2, 3, 4, 5]
    for i in range(0, len(side)):
        for k in range(0, len(dice)):
            minimo = dice[k]
            maximo = dice[k] * side[i]
            mediana = round((minimo + maximo) / 2, 1)
            dices = dice[k]
            sides = side[i]
            aux.append(minimo)
            aux.append(mediana)
            aux.append(maximo)
            aux.append(str(dices))
            aux.append(str(sides))
            valrs.append(aux)
            aux = []
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            aux.append(int(dados[i][k]))
        dados_i.append(aux)
        aux = []
    for i in range(0, len(dados_i)):
        dados_i[i].pop(-1)
    for i in range(0, len(dados_i)):
        aux.append(min(dados_i[i]))
        aux.append(mode(dados_i[i]))
        aux.append(round(mean(dados_i[i]), 1))
        aux.append(median(dados_i[i]))
        aux.append(max(dados_i[i]))
        trat.append(aux)
        aux = []
    for i in range(0, len(trat)):
        for k in range(0, len(valrs)):
            if trat[i][0] >= valrs[k][0] and valrs[k][2] >= trat[i][4]:
                if floor(valrs[k][1]) <= trat[i][1] <= ceil(valrs[k][1]) \
                        or floor(valrs[k][1]) <= trat[i][2] <= ceil(valrs[k][1]) \
                        or floor(valrs[k][1]) <= trat[i][3] <= ceil(valrs[k][1]):
                    resposta = valrs[k][3] + "d" + valrs[k][4]
                    respostas.append(resposta)
                    break

    print(*respostas)


dungeons_and_dragons_dice()
