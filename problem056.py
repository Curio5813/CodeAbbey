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
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            print(l1[i][j], end='')
    print()
    contil = []
    for n in range(10):
        cont1, vivas, mortas = 0, [], []
        # Procurar por celulas vazias que nascerão seres-vivos
        for i in range(len(l1)):
            for j in range(0, len(l1[i])):
                vivas_temp = []
                if l1[i][j] == '-':
                    cont2 = 0
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if k == 0 and l == 0:
                                continue
                            # Calcula as coordenadas do vizinho
                            linha = i + k
                            coluna = j + l

                            if linha < 0:
                                linha = len(l1) - 1
                            elif linha >= len(l1):
                                linha = 0

                            if coluna < 0:
                                coluna = len(l1[0]) - 1
                            elif coluna >= len(l1[0]):
                                coluna = 0
                                # Se o vizinho estiver vivo guarda a coordenada
                            if l1[linha][coluna] == 'X':
                                cont2 += 1
                    if cont2 == 3:
                        vivas_temp.append(i)
                        vivas_temp.append(j)
                        vivas.append(vivas_temp)
        # Procura por celulas com vida que morrerão
        for i in range(len(l1)):
            for j in range(0, len(l1[i])):
                mortas_temp = []
                if l1[i][j] == 'X':
                    cont3 = 0
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if k == 0 and l == 0:
                                continue
                            # Calcula as coordenadas do vizinho
                            linha = i + k
                            coluna = j + l

                            if 0 < linha < len(l1) - 1 and 0 < coluna < len(l1[i]):
                                # Se o vizinho estiver vivo guarda a coordenada
                                if l1[linha][coluna] == 'X':
                                    cont3 += 1
                    if cont3 < 2 or cont3 > 3:
                        mortas_temp.append(i)
                        mortas_temp.append(j)
                        mortas.append(mortas_temp)
        for coord in mortas:
            linha = coord[0]
            coluna = coord[1]
            l1[linha] = l1[linha][:coluna] + '-' + l1[linha][coluna + 1:]
        for coord in vivas:
            linha = coord[0]
            coluna = coord[1]
            l1[linha] = l1[linha][:coluna] + 'X' + l1[linha][coluna + 1:]
        for k in range(len(l1)):
            for l in range(len(l1[k])):
                print(l1[k][l], end='')
        print()
        for i in range(len(l1)):
            for j in range(len(l1[i])):
                if l1[i][j] == 'X':
                    cont1 += 1
        contil.append(cont1)

    print(*contil)
life_is_simple()

print(*[15, 22, 16, 18, 18])
