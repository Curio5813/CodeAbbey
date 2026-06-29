from csv import reader
from math import cos, sin, radians


def azimute_na_ilha_do_tesouro():
    """
    Um grupo de piratas teve a sorte de colocar as mãos no mapa da Ilha do Tesouro.

    Para sua decepção, o mapa não contém desenhos vagos com uma pequena cruz preta,
    mas apenas várias linhas como as seguintes:

    na praia sul da Ilha encontre o poste preso na areia com a placa Start anexado;
    azimute de giro 50 e vá 300 pés;
    prosseguir 500 pés por azimute 270;
    passo 150 pés a mais por azimute 300;
    cave aqui!
    Piratas ler na Wikipédia que azimuth 0 é a direção para o Norte, azimuth 90 é a
    direção para o Leste e assim por diante.

    No entanto, eles usam uma espécie de Navegador GPS no lugar de bússola. Em vez de
    direções, o dispositivo pode mostrar coordenadas ou deslocamentos em pés.

    Portanto, os piratas precisam resolver o seguinte problema: sugerir que o ponto do
    "pólo com a placa Start" é a origem do sistema de coordenadas com Y eixo apontando
    para o Norte e X eixo apontando para o East - quais são as coordenadas do ponto do
    tesouro?

    Dados de entrada estará em formato próximo às direções inscritas em um mapa:
    A primeira linha contém palavras Fique no poste com a placa START - você pode ignorar
    isso com segurança.
    As próximas linhas contêm palavras ir X pés por azimute Y - você deve extrair números deles.
    A última linha contém a frase Cave aqui!
    Resposta deve conter coordenadas do ponto onde o Tesouro está escondido, arredondadas para
    os números inteiros mais próximos.

    Exemplo:

    input data:
    Stand at the pole with the plaque START
    go 140 feet by azimuth 332
    go 460 feet by azimuth 78
    Dig here!

    answer:
    384 219
    :return:
    """
    arq = open("problem098.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    coordenada, coordenadas = [], []
    for i in range(0, len(l1)):
        l1[i][1] = int(l1[i][1])
        l1[i][5] = int(l1[i][5])
        coordenada.append(l1[i][1])
        coordenada.append(l1[i][5])
        coordenadas.append(coordenada)
        coordenada = []
    norte = 0
    leste = 90
    sul = 180
    oeste = 270
    x, y = 0, 0
    for i in range(0, len(coordenadas)):
        if oeste <= coordenadas[i][1] <= 360:
            angulo = coordenadas[i][1] - 270
            y += sin(radians(angulo)) * coordenadas[i][0]
            x -= cos(radians(angulo)) * coordenadas[i][0]
        if norte <= coordenadas[i][1] <= leste:
            angulo = coordenadas[i][1]
            y += cos(radians(angulo)) * coordenadas[i][0]
            x += sin(radians(angulo)) * coordenadas[i][0]
        if leste <= coordenadas[i][1] <= sul:
            angulo = coordenadas[i][1] - 180
            y += sin(radians(angulo)) * coordenadas[i][0]
            x += cos(radians(angulo)) * coordenadas[i][0]
        if sul <= coordenadas[i][1] <= oeste:
            angulo = coordenadas[i][1]
            y -= cos(radians(angulo)) * coordenadas[i][0]
            x += sin(radians(angulo)) * coordenadas[i][0]
    print(int(round(x, 0)), int(round(y, 0)))


azimute_na_ilha_do_tesour()
