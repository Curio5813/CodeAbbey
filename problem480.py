from csv import reader


def coin_payments():
    """
    No reino de Erewhon todos os pagamentos são feitos usando moedas.
    O valor de um pagamento pode variar consideravelmente em tamanho.
    Para acomodar esta grande variedade, o reino utiliza um grande número
    de denominações de moedas diferentes. Todas as denominações das moedas
    são números quadrados, então as moedas Erewhon (em ordem de tamanho)
    têm as denominações 1, 4, 9, 16, 25, 36... A unidade monetária é o zog.

    Ao fazer um pagamento no reino de Erewhon, há duas regras a serem observadas.
    O valor total das moedas utilizadas deve ser igual ao pagamento exigido.
    O pagamento deve ser feito de forma que a primeira moeda do pagamento tenha
    a maior denominação possível. A próxima moeda no pagamento deve ter a maior
    denominação possível (para o restante do pagamento) e assim por diante até
    que o pagamento seja concluído.

    Considere um pagamento de 19 zogs. A moeda de maior valor, que não seja maior
    que 19 zogs, tem um valor de 16 zogs. Os 3 zogs restantes devem ser pagos como
    três moedas de 1 zog. Então temos 19 = 16 + 1 + 1 + 1. Pode parecer que o
    pagamento de 19 poderia ser feito utilizando moedas com valores 9 + 9 + 1.
    Na verdade, isso usa uma moeda a menos do que a regra de pagamento correta.
    No entanto, as regras de pagamento são rigorosamente aplicadas, pelo que esta
    variação não seria aceite. A tabela a seguir mostra as moedas corretas a serem
    usadas para cada um dos pagamentos de 19 zogs a 35 zogs inclusive. A contagem
    de moedas para cada pagamento é mostrada entre colchetes.

    19 = 16 + 1 + 1 + 1  (4)
    20 = 16 + 4  (2)
    21 = 16 + 4 + 1  (3)
    22 = 16 + 4 + 1 + 1  (4)
    23 = 16 + 4 + 1 + 1 + 1  (5)
    24 = 16 + 4 + 4  (3)
    25 = 25  (1)
    26 = 25 + 1  (2)
    27 = 25 + 1 + 1  (3)
    28 = 25 + 1 + 1 + 1  (4)
    29 = 25 + 4  (2)
    30 = 25 + 4 + 1  (3)
    31 = 25 + 4 + 1 + 1  (4)
    32 = 25 + 4 + 1 + 1 + 1  (5)
    33 = 25 + 4 + 4  (3)
    34 = 25 + 9  (2)
    35 = 25 + 9 + 1  (3)

    Se somarmos o número de moedas necessárias para cada um destes pagamentos
    obtemos um total de 53 moedas. Esta é a contagem de moedas para o intervalo
    de pagamentos de 19 a 35.

    No problema real, você receberá uma variedade de pagamentos de N1 a N2 inclusive.
    Você é solicitado a encontrar a contagem de moedas para esta faixa de pagamentos.
    O intervalo fornecido será muito maior do que neste pequeno exemplo. Entretanto,
    o valor de N2 não excederá 160000000000 (16 x 10^10).

    Descrição de entrada/saída: A primeira e única linha dos dados de entrada conterá
    dois inteiros N1 e N2, separados por um espaço. Sua resposta é a contagem de
    moedas para a faixa de pagamentos de N1 a N2 inclusive.
    :return:
    """
    arq = open('problem480.csv')
    l1 = list(reader(arq, delimiter=' '))
    entrada = []
    for i in range(0, len(l1)):
        for j in range(0, len(l1[i])):
            entrada.append(int(l1[i][j]))
    inicio, fim = entrada[0], entrada[1]
    moedas = []
    for i in range(1, fim + 1):
        if i * i > fim:
            break
        moedas.append(i * i)
    moedas.reverse()
    qtd1, qtd2 = 0, 0
    for i in range(inicio, fim + 1):
        valor = i
        print(valor, end=' ')
        for j in range(len(moedas)):
            for k in range(len(moedas)):
                if moedas[j] > valor:
                    break
                elif  valor >= moedas[j]:
                    print(moedas[j], end=' ')
                    valor -= moedas[j]
                    qtd1 += 1
        print()
        print(qtd1)
        qtd2 += qtd1
        qtd1 = 0
    print(qtd2)


coin_payments()
