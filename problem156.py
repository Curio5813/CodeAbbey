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

    All the card numbers would be 16 digits long (this is the most common length even in fairytales.

    Input data contain a list of workers who have their card numbers incorrect.
    Next lines contain a single card number each. If the number contains "?" (question mark) instead
    of some digit - this digit should be restored. If all digits are present, then "swap-error" should
    be fixed.
    Answer should contain a list of "fixed" card numbers.
    :return:
    """
    arq = open("problem156.csv")
    dados = reader(arq)
    dados = list(dados)
    print(dados)
    return dados


def processing_1(dados):
    """
    First processing input data.
    :param dados:
    :return:
    """
    aux, treat, idx_main = [], [], []
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            for j in range(0, len(dados[i][k])):
                if dados[i][k][j] == '?':
                    aux.append(10)
                    idx_main.append(i)
                else:
                    aux.append(int(dados[i][k][j]))
            treat.append(aux)
            aux = []
    print(treat)
    return treat


def processing_2(dados):
    """
    Second processing input data.
    :param dados:
    :return:
    """
    aux, treat, idx_main = [], [], []
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            for j in range(0, len(dados[i][k])):
                if dados[i][k][j] == '?':
                    aux.append(10)
                    idx_main.append(i)
                else:
                    aux.append(int(dados[i][k][j]))
            treat.append(aux)
            aux = []
    print(idx_main)
    return idx_main


def processing_3(treat):
    """
    Fourth processing treating data.
    :param treat:
    :return:
    """
    aux, algol1 = [], []
    for i in range(0, len(treat)):
        treat[i].reverse()
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
    print(algol2)
    return algol2


def analise_1_1(algol1):
    """
    First analise from swap-error.
    :param algol1:
    :return:
    """
    aux, analise1, cont, algols = [], [], 0, []
    for i in range(0, len(algol1)):
        for k in range(0, len(algol1[i])):
            aux.append(algol1[i][k])
            cont += 1
            if cont > 0 and cont % 4 == 0:
                algols.append(aux)
                aux = []
        analise1.append(algols)
        algols = []
    print(analise1)
    return analise1


def analise_1_2(analise1):
    """
    Working...
    :param analise1:
    :return:
    """


def analise_2_1(algol2):
    """
    First analise from missed numbers.
    :param algol2:
    :return:
    """
    aux, cont, algols, analise2 = [], 0, [], []
    for i in range(0, len(algol2)):
        for k in range(0, len(algol2[i])):
            aux.append(algol2[i][k])
            cont += 1
            if cont > 0 and cont % 4 == 0:
                algols.append(aux)
                aux = []
        analise2.append(algols)
        algols = []
    print(analise2)
    return analise2


def analise_2_2(analise2):
    """
    This function putting zeros where there is a number missed.
    :param analise2:
    :return:
    """
    idx1 = []
    for i in range(0, len(analise2)):
        for k in range(0, len(analise2[i])):
            for j in range(0, len(analise2[i][k])):
                if analise2[i][k][j] == 10:
                    analise2[i][k][j] = 0
                    idx1.append(j)
                    break
    print(idx1)
    return idx1


def analise_2_3(analise2):
    """
    This function count the sum for each card numbers where misses numbers
    are zeros.
    :param analise2:
    :return:
    """
    soma, somas1 = 0, []
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
    print(somas1)
    return somas1


def analise_2_4(idx1, somas1):
    """
    This function analise about missed number by taking the sum of numbers and
    finding the missed numbers who the sum is multiple of 10.
    :param idx1:
    :param somas1:
    :return:
    """
    numbers = []
    for i in range(0, len(somas1)):
        if idx1[i] % 2 == 0:
            for j in range(0, 10):
                if (somas1[i] + j) % 10 == 0:
                    numbers.append(j)
                    break
        elif idx1[i] % 2 != 0:
            for j in range(0, 10):
                if (j * 2 + somas1[i]) % 10 == 0:
                    numbers.append(j)
                    break
                if (j * 2) >= 10:
                    m = j * 2 - 9
                    if (m + somas1[i]) % 10 == 0:
                        numbers.append(j)
                        break
    print(numbers)
    return numbers


def analise_2_5(dados, idx_main, algol2, numbers):
    """
    This function putting the fixed missed numbers card into the data.
    :param dados:
    :param idx_main:
    :param algol2:
    :param numbers:
    :return:
    """
    aux_str, str_algol = "", []
    for i in range(0, len(algol2)):
        for k in range(0, len(algol2[i])):
            if algol2[i][k] == 10:
                algol2[i][k] = numbers[i]
    for i in range(0, len(algol2)):
        algol2[i].reverse()
    for i in range(0, len(algol2)):
        for k in range(0, len(algol2[i])):
            aux_str += str(algol2[i][k])
        str_algol.append(aux_str)
        aux_str = ""
    for i in range(0, len(idx_main)):
        for k in range(0, len(dados)):
            for j in range(0, len(dados[k])):
                if k == idx_main[i]:
                    dados[k][j] = str_algol[i]
    return dados


def fixed_numbers(dados):
    """
    Output fixed numbers cards.
    :return:
    """
    for i in range(0, len(dados)):
        for k in range(0, len(dados[i])):
            print(dados[i][k], end=" ")


fixed_numbers(analise_2_5(luhn_algorithm(), processing_2(luhn_algorithm()),
                          processing_4(processing_1(luhn_algorithm())),
                          analise_2_4(analise_2_2(analise_2_1(processing_4
                                                              (processing_1(luhn_algorithm())))),
                                      analise_2_3(analise_2_1(processing_4
                                                              (processing_1(luhn_algorithm())))))))
