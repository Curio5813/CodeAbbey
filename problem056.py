from copy import deepcopy


def life_is_simple():
    """
    O jogo de Vida de John Conway é jogado em uma grade. No início colocamos
    vários "organismos" em algumas células (apenas um organismo por célula),
    deixando outras células vazias. As células que se tocam lateralmente ou
    nos cantos são vizinhas,portanto, cada organismo pode ter 0 para 8 vizinhos.

    Depois disso, a cada turno a colônia de organismos evolui pelas seguintes regras:

    qualquer organismo que tenha menos de 2 ou mais de 3 os vizinhos morrerão (não
    passando para a próxima curva);
    ao mesmo tempo em cada célula vazia, que é cercada exatamente por 3 organismos
    vizinhos, nasce um novo.
    É importante que o nascimento e a morte sejam realizados simultaneamente. Então,
    ao programar você precisa de um trabalho como este:

    marque todos os lugares onde uma nova vida nascerá;
    marque todos os organismos que morrerão;
    remover todos os organismos marcados;
    preencha todas as células vazias marcadas com novos organismos.
    Em vez de marcar células, você pode armazenar suas coordenadas em duas matrizes ou
    listas dedicadas para processá-las posteriormente.

    Vejamos um exemplo:

    - - - - -      - - - - -      - - - - -
    - - - - -      - - X - -      - - - - -
    - X X X -  =>  - - X - -  =>  - X X X -
    - - - - -      - - X - -      - - - - -
    - - - - -      - - - - -      - - - - -

    Aqui está uma colônia de 3 organismos. Obviamente, na primeira curva dois deles
    (esquerda e direita) deveriam morrer. No entanto,antes de morrer, elas participarão
    do parto de outras duas. Na verdade, as células vazias logo acima da central e logo
    abaixo dela têm exatamente 3 vizinhos. Então, após a primeira volta, a colônia parece
    a mesma, mas girada em 90°.É claro que após o segundo movimento a configuração
    retornará exatamente à forma como era inicialmente.

    Neste problema você executará a configuração fornecida por 5 turnos e imprimirá o
    número de organismos após cada etapa.

    Input data will contain 5 lines of 7 characters each. They represent a 5 by 7 fragment
    of the game field.
    Dash characters "-" represent empty cells, while each "X" represent a cell containing
    a live organism.
    Answer should contain 5 values separated by spaces - the amounts of live organisms after
    each turn.

    Example:

    input data:
    -------
    ---XX--
    -XXX---
    -------
    -------

    answer:
    6 5 3 2 0
    :return:
    """
    arq = open('problem056.csv')
    l1 = list(arq)
    for n in range(5):
        cont, vivas, vivas_vert, vivas_lat, mortas, mortas_1, mortas_2, mortas_1_1, mortas_2_1, mortas_3, mortas_4, teste, testes = 0, [], [], [], [], [], [], [], [], [], [], [], []
        # print('Ok!')
        for i in range(len(l1)):
            for j in range(len(l1[i])):
                if l1[i][j] == 'X':
                    teste.append(i)
                    teste.append(j)
                    testes.append(teste)
                    teste = []
        # print(testes)
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 1 and 0 < j < len(l1[0]) - 1:
                    if l1[i][j] == 'X' and l1[i][j - 1] == 'X' and l1[i][j + 1] == 'X' and l1[i - 1][j] == '-' and l1[i + 1][j] == '-':
                        vivas_vert.append(i - 1)
                        vivas_vert.append(j)
                        vivas.append(vivas_vert)
                        vivas_vert = []
                        vivas_vert.append(i + 1)
                        vivas_vert.append(j)
                        vivas.append(vivas_vert)
                        vivas_vert = []
                        # print('Ok01')
                        break
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 1 and 0 < j < len(l1[0]) - 1:
                    if l1[i][j] == 'X' and l1[i - 1][j] == 'X' and l1[i + 1][j] == 'X' and l1[i][j - 1] == '-' and l1[i][j + 1] == '-':
                        vivas_lat.append(i)
                        vivas_lat.append(j - 1)
                        vivas.append(vivas_lat)
                        vivas_lat = []
                        vivas_lat.append(i)
                        vivas_lat.append(j + 1)
                        vivas.append(vivas_lat)
                        vivas_lat = []
                        # print('Ok02')
                        break
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 1 and 0 < j < len(l1[0]) - 1:
                    if l1[i][j] == 'X' and l1[i][j - 1] == '-' and l1[i - 1][j] == '-' and l1[i + 1][j] == '-':
                        mortas_1.append(i)
                        mortas_1.append(j)
                        mortas.append(mortas_1)
                        mortas_1 = []
                        # print('Ok10')
                        break
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 1 and 0 < j < len(l1[0]) - 1:
                    if l1[i][j] == 'X' and l1[i][j + 1] == '-' and l1[i - 1][j] == '-' and l1[i + 1][j] == '-':
                        mortas_2.append(i)
                        mortas_2.append(j)
                        mortas.append(mortas_2)
                        mortas_2 = []
                        # print('Ok12')
                        break
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 1 and 0 < j < len(l1[0]) - 1:
                    if l1[i][j] == 'X' and l1[i - 1][j] == '-' and l1[i][j - 1] == '-' and l1[i][j + 1] == '-':
                        mortas_1_1.append(i)
                        mortas_1_1.append(j)
                        mortas.append(mortas_1_1)
                        mortas_1_1 = []
                        # print('Ok10')
                        break
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 1 and 0 < j < len(l1[0]) - 1:
                    if l1[i][j] == 'X' and l1[i + 1][j] == '-' and l1[i][j - 1] == '-' and l1[i][j + 1] == '-':
                        mortas_2_1.append(i)
                        mortas_2_1.append(j)
                        mortas.append(mortas_2_1)
                        mortas_2_1 = []
                        # print('Ok12')
                        break
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 2 and 0 < j < len(l1[0]) - 2:
                    if l1[i][j] == 'X' and l1[i][j - 1] == 'X' and l1[i][j - 2] and l1[i][j + 1] == 'X' and l1[i][j + 2] == 'X':
                        mortas_3.append(i)
                        mortas_3.append(j)
                        mortas.append(mortas_3)
                        mortas_3 = []
                        # print('Ok2')
                        break
        for i in range(len(l1)):
            for j in range(i, len(l1[i])):
                if 0 < i < len(l1) - 2 and 0 < j < len(l1[0]) - 2:
                    if l1[i][j] == 'X' and l1[i - 1][j] == 'X' and l1[i - 2][j] == 'X' and l1[i + 1][j] and l1[i + 2][j] == 'X':
                        # print('Ok2')
                        mortas_4.append(i)
                        mortas_4.append(j)
                        mortas.append(mortas_4)
                        mortas_4 = []
                        break
        print('\n')
        # print(mortas, 'Opa!')
        for coord in mortas:
            linha = coord[0]
            coluna = coord[1]
            l1[linha] = l1[linha][:coluna] + '-' + l1[linha][coluna + 1:]
        print('\n')
        # print(vivas, 'Epa!')
        for coord in vivas:
            linha = coord[0]
            coluna = coord[1]
            l1[linha] = l1[linha][:coluna] + 'X' + l1[linha][coluna + 1:]
        for i in range(len(vivas)):
            for j in range(len(vivas[i])):
                if i in vivas[i] and j in vivas[i]:
                    l1[i] = l1[i][:j] + 'X' + l1[i][j + 1:]
        for i in range(len(l1)):
            for j in range(len(l1[i])):
                print(l1[i][j], end='')
        for i in range(len(l1)):
            for j in range(len(l1[i])):
                if l1[i][j] == 'X':
                    cont += 1
        print(cont)


life_is_simple()
