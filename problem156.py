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
    return analise1


def analise_1_2(analise1):
    """
    This function calculate each part of the sum in the set of numbers cards
    using the algorithm.
    :param analise1:
    :return:
    """
    print(len(analise1))
    print(analise1)
    soma, somas, somas1 = 0, [], []
    for i in range(0, len(analise1)):
        analise1[i].reverse()
        print(analise1[i], end=" ")
        for k in range(0, len(analise1[i])):
            a, b, c, d = analise1[i][k][0], analise1[i][k][1], analise1[i][k][2], analise1[i][k][3]
            b = b * 2
            if b >= 10:
                b -= 9
            d = d * 2
            if d >= 10:
                d -= 9
            soma = a + b + c + d
            somas.append(soma)
        somas1.append(somas)
        somas = []
    return somas1


def analise_1_3(analise1, somas1):
    """
    This function find the numbers swapped.
    :param analise1:
    :param somas1
    :return:
    """
    print("\n")
    print(somas1)
    print(len(somas1))
    cont, k, r, s, t, u, m, n, soma, aux, numbers1, aux_idx, idx1 = 0, \
        0, 0, 0, 0, 0, 0, 0, 0, [], [], [], []
    for i in range(0, len(analise1)):
        analise1[i].reverse()
        for k in range(0, len(analise1[i])):
            r, s, t, u = analise1[i][k][0], analise1[i][k][1], analise1[i][k][2], analise1[i][k][3]
            t, u = u, t
            m = s * 2
            if m >= 10:
                m -= 9
            n = u * 2
            if n >= 10:
                n -= 9
            soma = r + m + t + n
            somas = soma + sum(somas1[i]) - somas1[i][k]
            if somas % 10 == 0:
                aux.append(r)
                aux.append(s)
                aux.append(t)
                aux.append(u)
                numbers1.append(aux)
                aux_idx.append(i)
                aux_idx.append(k)
                idx1.append(aux_idx)
                aux = []
                aux_idx = []
                break
            r, s, t, u = analise1[i][k][0], analise1[i][k][1], analise1[i][k][2], analise1[i][k][3]
            s, t = t, s
            m = s * 2
            if m >= 10:
                m -= 9
            n = u * 2
            if n >= 10:
                n -= 9
            soma = r + m + t + n
            somas = soma + sum(somas1[i]) - somas1[i][k]
            if somas % 10 == 0:
                aux.append(r)
                aux.append(s)
                aux.append(t)
                aux.append(u)
                numbers1.append(aux)
                aux_idx.append(i)
                aux_idx.append(k)
                idx1.append(aux_idx)
                aux = []
                aux_idx = []
                break
            r, s, t, u = analise1[i][k][0], analise1[i][k][1], analise1[i][k][2], analise1[i][k][3]
            r, s = s, r
            m = s * 2
            if m >= 10:
                m = m - 9
            n = u * 2
            if n >= 10:
                n -= 9
            soma = r + m + t + n
            somas = soma + sum(somas1[i]) - somas1[i][k]
            if somas % 10 == 0:
                aux.append(r)
                aux.append(s)
                aux.append(t)
                aux.append(u)
                numbers1.append(aux)
                aux_idx.append(i)
                aux_idx.append(k)
                idx1.append(aux_idx)
                aux = []
                aux_idx = []
                break
    print(numbers1)
    print(len(numbers1))
    return numbers1


def analise_2(dados, idx_missed, algol2):
    """
    This fuction calculate the missed numbers and put it in the correct place
    in the numbers cards.
    :param dados:
    :param idx_missed
    :param algol2:
    :return:
    """
    aux, cont, algols, analise2, idx1, soma, somas1, numbers2, aux_str,\
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
    print(analise2)
    print(len(analise2))
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
        for k in range(0, len(dados)):
            for j in range(0, len(dados[k])):
                if k == idx_missed[i]:
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


processing_2_1(luhn_algorithm())
analise_1_3(analise_1_1(processing_3(processing_1(luhn_algorithm()))),
            analise_1_2(analise_1_1(processing_3(processing_1(luhn_algorithm())))))
fixed_numbers(analise_2(luhn_algorithm(), processing_2_2(luhn_algorithm()),
                        processing_4(processing_1(luhn_algorithm()))))
