from csv import reader
from collections import deque


def chords_of_music():
    """
    [https://codeabbey.github.io/data/chords_of_music.jpg]!Imagem

    Vamos aprender um pouco mais sobre música.

    Você provavelmente sabe que a música pode soar alegre e levemente, ou sensualmente
    melancólica ou até triste.

    Esse "temperamento" da música é baseado em relações matemáticas muito simples! Prepare-se
    para que este grande mistério seja revelado! :)

    Do Tom e Notas você pode ter aprendido algumas coisas importantes para esta tarefa:

    que as notas musicais seguem em passos iguais (semitons) na escala logarítmica da
    frequência sonora;
    que 12 etapas completas octave, depois disso as notas se repetem, mas com frequência
    duplicada;
    que as notas têm 12 nomes para distingui-los no escopo da oitava (e as oitavas também têm
    seus nomes ou números).
    Aqui estão os nomes das notas novamente, colocados em ordem com um passo de semitom entre
    eles:

    C  C#  D  D#  E  F  F#  G  G#  A  A#  B
    Existe um conceito importante de chord - a união de várias notas tocadas simultaneamente
    ou fechadas uma após a outra. Discutiremos apenas dois acordes principais - major e minor.

    Ambos os acordes consistem em três notas de tom diferente. Eles são chamados root, third e
    fifth. Na forma pura do acorde o root tem o tom mais baixo e o fifth tem o mais alto.

    E ainda mais, eles têm uma quantidade precisa de etapas entre eles:

    fifth tem tom 7 passos (semitons) mais altos que root;
    third é qualquer um 3 ou 4 degraus mais altos que root;
    se third é 4 degraus mais altos que root então é major acorde;
    e em minor acorde third é apenas 3 degraus mais altos que o root.
    Então, se quisermos construir o acorde maior com nota D como uma raiz (por exemplo D-major)
    precisamos jogar D, então F# (qual é 4 passos de D) e finalmente A (que é 3 passos de F# e 7
    de D).

    A tabela abaixo mostra as notas de D-major e D-minor acordes para que você mesmo possa contar
    os passos.

              | C  C#  D  D#  E  F  F#  G  G#  A  A#  B
          ----+-------------------------------------------
    D-major   |        *      4     *     3    *
              |
    D-minor   |        *    3    *      4      *
    Claro que se ao construir um acorde chegamos ao final da oitava, simplesmente passamos para a
    próxima oitava, por exemplo, para A-minor então as notas seriam A, C e E.

    Grande Mistério
    And now here is the secret - major chords make "happy" and "joyful" sound, while minor chords
    bear melancholic and even mournful expression. You may found sample sounds in the wikipedia
    page about 3-note chords.

    Now another curious thing - any note of the chord could be shifted by the whole octave (or
    several) up or down - the chord will retain its temper. E.g. raising or lowering any note
    by k*12 steps does not break the chord!

    Popular example of this is an Inverted chord where, for example, the root is raised one
    octave up. Sometimes they are distinguished from pure chords, but generally speaking they
    could substitute one another for example if it is easier to play without breaking fingers.

    Another example is playing additional sound to the chord - the same as root but lowered octave
    or two - such a base bass note which may be useful to audibly highlight accents while
    accompanying vocal etc.

    Problem statement
    You are given several notes described by their numbers according to MIDI-standard - C of the
    0-th octave is 0, D in the same octave is 2, B is 11 and so on, so that 64 means E of the
    5-th octave.

    The task is to determine what chord these notes represent.

    Input data contain the number of test-cases in the first line.
    Next lines contain from 3 or more integers - numbers of notes played.
    Answer should contain respective chord names in form C-minor, F#-major or the word other
    in cases when notes do not form one of these two chords at all.

    Example:

    input data:
    3
    87 73 64 61
    46 37 53 58 70
    44 48 51 56 32

    answer:
    other A#-minor G#-major
    :return:
    """
    # Notas Musicas - Começando de C
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    # Notas Musicais - Começando do A - Fundamental
    notas_fundamental = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G',
                         'G#']
    notas_midi, notas_cifra = [], []
    # Tratamento dos dados de entrada pelo arquivo .csv
    arq = open('problem173.csv')
    acorde_midi = reader(arq, delimiter=' ')
    acorde_midi = list(acorde_midi)
    acorde_midi.pop(0)
    # Notas Musicas em Notação de Cifra (128 Notas)
    for i in range(10):
        notas_cifra.extend(notas)
    notas_cifra.extend(notas[0:8])
    for i in range(len(notas_cifra)):
        notas_midi.append(i)
    # Acordes tocados no padrão MIDI (Tratamento de Dados)
    for i in range(len(acorde_midi)):
        for j in range(len(acorde_midi[i])):
            acorde_midi[i][j] = int(acorde_midi[i][j])
        acorde_midi[i].sort()
    # Acordes tocados notação Cifra
    acorde_cifra, temp = [], []
    for i in range(len(acorde_midi)):
        for j in range(len(acorde_midi[i])):
            # Pegando a primeira nota
            if len(temp) == 0:
                temp.append(notas_cifra[acorde_midi[i][j]])
            # Pegando só tríades dos acordes
            if len(temp) > 0 and notas_cifra[acorde_midi[i][j]] not in temp:
                temp.append(notas_cifra[acorde_midi[i][j]])
        temp.sort()
        acorde_cifra.append(temp)
        temp = []
    semiton_1, semiton_2, semiton_3 = 0, 0, 0
    # Achando Tom e Modo (Maior ou Menor) ou Atonalidade
    for i in range(len(acorde_cifra)):
        flag = False
        # Usando deque da biblioteca collections para rotacionar tríades de acordes
        fila = deque(acorde_cifra[i])
        tamanho = len(fila)
        for j in range(tamanho):
            # Atualizando lista para pegar inversão de acordes
            lista_atual = list(fila)
            for k in range(len(notas_fundamental)):
                if lista_atual[0] == notas_fundamental[k]:
                    semiton_1 = k + 1
                if lista_atual[1] == notas_fundamental[k]:
                    semiton_2 = k + 1
                if lista_atual[2] == notas_fundamental[k]:
                    semiton_3 = k + 1
            # Cálculo das distâncias considerando a escala circular (módulo 12)
            diff_1 = (semiton_2 - semiton_1) % 12
            diff_2 = (semiton_3 - semiton_1) % 12
            # (Fundamental, Terça e Quinta)
            # Menor: terça menor (3 semitons) e quinta justa (7 semitons)
            # Maior: terça maior (4 semitons) e quinta justa (7 semitons)
            if diff_1 == 3 and diff_2 == 7:
                print(f"{lista_atual[0]}-minor")
                flag = True
                break
            if diff_1 == 4 and diff_2 == 7:
                print(f"{lista_atual[0]}-major")
                flag = True
                break
            fila.rotate(-1)
        if not flag:
            print("other")


chords_of_music()
