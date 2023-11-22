from csv import reader


def luhn_algorithm():
    """
    The method is named after Hans Peter Luhn who have proposed it.
    The main idea of the algorithm is to check most common types of
    mistakes - and on the other hand to be simple enough, i.e:

    * to be so simple that it could be calculated with (or without)
      paper and pencil, or with mechanic device;
    * detect mistake in any single digit;
    * detect accidental swap of two adjacent digits.

    And here are the steps of the algorithm:

    1. We should sum up all digits starting from the end.
    2. However each second digit (2nd from the end, 4th from the end
       and so on) is not added "as is" - instead it is multiplied by
       two (if the result contains more than one digit - sum its digits
       - or simply subtract 9 from it).
    3. If result is not a multiple of 10, then the number is incorrect.
       For example if we have a number 4123 1759 0498 1754 then we should
       sum up the following values (going from the end):

    For example if we have a number 4123 1759 0498 1754 then we should sum
    up the following values (going from the end):

    4+(5*2-9)+7+(1*2) + 8+(9*2-9)+4+(0*2) + 9+(5*2-9)+7+(1*2) + 3+(2*2)+1+(4*2) = 70
    Since 70 is divisible by 10 then probably the number is valid.

    To create correct number usually the last digit is really check digit - i.e. it
    doesn't store any business information but instead is chosen so that the whole
    number gives a proper checksum.

    All the card numbers would be 16 digits long (this is the most common length even
    in fairytales.

    Input data contain a list of workers who have their card numbers incorrect.
    Next lines contain a single card number each. If the number contains "?" (question mark)
    instead
    of some digit - this digit should be restored. If all digits are present, then "swap-error"
    should be fixed.
    Answer should contain a list of "fixed" card numbers.
    :return:
    """
    arq = open("problem156.csv")
    dados = reader(arq)
    dados = list(dados)
    return dados


def processing_1(dados):
    """
    First processing input data.
    :param dados:
    :return:
    """
    aux, treat = [], []
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            for j in range(0, len(dados[i][k])):
                if dados[i][k][j] == '?':
                    aux.append(10)
                else:
                    aux.append(int(dados[i][k][j]))
            treat.append(aux)
            aux = []
    return treat


def processing_2_1(dados):
    """
    Second processing input data. Find the index wich the numbers is missed.
    :param dados:
    :return:
    """
    idx_swap = []
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            if '?' not in dados[i][k]:
                idx_swap.append(i)
    return idx_swap


def processing_2_2(dados):
    """
    Second processing input data. Find the index wich the numbers is missed.
    :param dados:
    :return:
    """
    idx_missed = []
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            for j in range(0, len(dados[i][k])):
                if dados[i][k][j] == '?':
                    idx_missed.append(i)
    return idx_missed


def processing_3(treat):
    """
    Third processing treating data.
    :param treat:
    :return:
    """
    aux, algol1 = [], []
    for i in range(0, len(treat)):
        if 10 not in treat[i]:
            algol1.append(treat[i])
    return algol1


def processing_4(treat):
    """
    Third processing treating data.
    :param treat:
    :return:
    """
    aux, algol2 = [], []
    for i in range(0, len(treat)):
        treat[i].reverse()
        if 10 in treat[i]:
            algol2.append(treat[i])
    return algol2


def analise_1_1(algol1):
    """
    First analise from swap-error.
    :param algol1:
    :return:
    """
    k, soma, somas, algol1_1, str_num, str_algol1,  = 0, 0, [], [], "", []
    for i in range(0, len(algol1)):
        mix = algol1[i].copy()
        while k < len(algol1[i]) - 1:
            algol1[i] = mix.copy()
            algol1[i][k], algol1[i][k + 1] = algol1[i][k + 1], algol1[i][k]
            algol1[i].reverse()
            for j in range(0, len(algol1[i]), 4):
                a, b, c, d = algol1[i][j], algol1[i][j + 1], algol1[i][j + 2], algol1[i][j + 3]
                m = b * 2
                if m >= 10:
                    m -= 9
                n = d * 2
                if n >= 10:
                    n -= 9
                soma = a + m + c + n
                somas.append(soma)
            if sum(somas) % 10 == 0:
                algol1[i].reverse()
                algol1_1.append(algol1[i])
                k = 0
                break
            else:
                somas = []
            k += 1
    for i in range(0, len(algol1_1)):
        for k in range(0, len(algol1_1[i])):
            str_num += str(algol1_1[i][k])
        str_algol1.append(str_num)
        str_num = ""
    return str_algol1


def analise_1_2(str_algol1, dados, idx_swap):
    """
    This function find the numbers swapped.
    :param str_algol1:
    :param dados:
    :param idx_swap:
    :return:
    """
    dados1 = []
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            dados1.append(*dados[i])
    for i in range(0, len(idx_swap)):
        for k in range(0, len(dados1)):
            if k == idx_swap[i]:
                dados1[k] = str_algol1[i]
    return dados1


def analise_2(dados1, idx_missed, algol2):
    """
    This fuction calculate the missed numbers and put it in the correct place
    in the numbers cards.
    :param dados1:
    :param idx_missed
    :param algol2:
    :return:
    """
    aux, cont, algols, analise2, idx1, soma, somas1, numbers2, aux_str, \
        str_algol = [], 0, [], [], [], 0, [], [], "", []
    for i in range(0, len(algol2)):
        for k in range(0, len(algol2[i])):
            aux.append(algol2[i][k])
            cont += 1
            if cont > 0 and cont % 4 == 0:
                algols.append(aux)
                aux = []
        analise2.append(algols)
        algols = []
    for i in range(0, len(analise2)):
        for k in range(0, len(analise2[i])):
            for j in range(0, len(analise2[i][k])):
                if analise2[i][k][j] == 10:
                    analise2[i][k][j] = 0
                    idx1.append(j)
                    break
    for i in range(0, len(analise2)):
        for k in range(0, len(analise2[i])):
            if analise2[i][k][1] * 2 < 10 and analise2[i][k][3] * 2 < 10:
                soma += analise2[i][k][0] + analise2[i][k][1] * 2 + analise2[i][k][2] + \
                        analise2[i][k][3] * 2
            elif analise2[i][k][1] * 2 >= 10 and analise2[i][k][3] * 2 >= 10:
                soma += analise2[i][k][0] + analise2[i][k][1] * 2 - 9 + analise2[i][k][2] + \
                        analise2[i][k][3] * 2 - 9
            elif analise2[i][k][1] * 2 >= 10 > analise2[i][k][3] * 2:
                soma += analise2[i][k][0] + analise2[i][k][1] * 2 - 9 + analise2[i][k][2] + \
                        analise2[i][k][3] * 2
            elif analise2[i][k][1] * 2 < 10 <= analise2[i][k][3] * 2:
                soma += analise2[i][k][0] + analise2[i][k][1] * 2 + analise2[i][k][2] + \
                        analise2[i][k][3] * 2 - 9
        somas1.append(soma)
        soma = 0
    for i in range(0, len(somas1)):
        if idx1[i] % 2 == 0:
            for j in range(0, 10):
                if (somas1[i] + j) % 10 == 0:
                    numbers2.append(j)
                    break
        elif idx1[i] % 2 != 0:
            for j in range(0, 10):
                if (j * 2 + somas1[i]) % 10 == 0:
                    numbers2.append(j)
                    break
                if (j * 2) >= 10:
                    m = j * 2 - 9
                    if (m + somas1[i]) % 10 == 0:
                        numbers2.append(j)
                        break
    for i in range(0, len(algol2)):
        for k in range(0, len(algol2[i])):
            if algol2[i][k] == 10:
                algol2[i][k] = numbers2[i]
    for i in range(0, len(algol2)):
        algol2[i].reverse()
    for i in range(0, len(algol2)):
        for k in range(0, len(algol2[i])):
            aux_str += str(algol2[i][k])
        str_algol.append(aux_str)
        aux_str = ""
    for i in range(0, len(idx_missed)):
        for k in range(0, len(dados1)):
            if k == idx_missed[i]:
                dados1[k] = str_algol[i]
    return dados1


def fixed_numbers(dados1):
    """
    Output fixed numbers cards.
    :return:
    """
    for i in range(0, len(dados1)):
        print(dados1[i], end=" ")


fixed_numbers(analise_2(analise_1_2(analise_1_1(processing_3(processing_1(luhn_algorithm()))),
                                    luhn_algorithm(), processing_2_1(luhn_algorithm())),
                        processing_2_2(luhn_algorithm()), processing_4(processing_1(luhn_algorithm()))))

