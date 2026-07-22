from csv import reader
from collections import Counter, deque


def chords_of_Music():
    """

    :return:
    """
    # Notas Musicas
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    notas_midi, notas_cifra = [], []
    # Tratamento dos dados de entrada pelo arquivo .csv
    arq = open('problem173.csv')
    acorde_midi = reader(arq, delimiter=' ')
    acorde_midi = list(acorde_midi)
    # print(acorde_midi)
    acorde_midi.pop(0)
    #print(acorde_midi)
    # Notas Musicas em Notação de Cifra (128 Notas)
    for i in range(10):
        notas_cifra.extend(notas)
    notas_cifra.extend(notas[0:8])
    print(notas_cifra)
    # Padrão MIDI de Notas Musicais
    for i in range(len(notas_cifra)):
        notas_midi.append(i)
    # Acordes tocados no padrão MIDI (Tratamento de Dados)
    # print(notas_midi)
    for i in range(len(acorde_midi)):
        for j in range(len(acorde_midi[i])):
            acorde_midi[i][j] = int(acorde_midi[i][j])
        acorde_midi[i].sort()
        acorde_midi[i].reverse()
    print(acorde_midi)
    # Acordes tocados notação Cifra
    acorde_cifra, temp = [], []
    for i in range(len(acorde_midi)):
        for j in range(len(acorde_midi[i])):
            temp.append(notas_cifra[acorde_midi[i][j]])
        acorde_cifra.append(temp)
        temp = []
    print(acorde_cifra)
    for i in range(len(acorde_cifra)):
        tom = acorde_cifra[i][0]
        print(tom)
        for j in range(len(acorde_cifra[i])):
            semiton_0 = notas_cifra.index(acorde_cifra[i][0])
            for k in range(semiton_0, len(notas_cifra)):
                semiton_1 = notas_cifra.index(acorde_cifra[i][j + 1])
                diff = semiton_1 - semiton_0
                if diff == 2 or diff == 4:
                    print(f"{tom}-minor")
                    print('Ok02', diff)
                elif diff == 3 or diff == 5:
                    print(f"{tom}-major")
                    print('Ok03', diff)
            for k in range(len(notas_cifra), semiton_0 - 1, -1):
                semiton_1 = notas_cifra.index(acorde_cifra[i][j + 1])
                diff = semiton_1 - semiton_0
                if diff == 2 or diff == 4:
                    print(f"{tom}-minor")
                    print('Ok02', diff)
                elif diff == 3 or diff == 5:
                    print(f"{tom}-major")
                    print('Ok03', diff)
            else:
                print('other')
                print('Ok04', diff)
                break


chords_of_Music()
