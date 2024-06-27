from math import log2
from csv import reader


def frequency_of_notes():
    """
    Data entrance.
    :return:
    """
    arq = open("problem089.csv")
    fqc = reader(arq, delimiter=" ")
    fqc = list(fqc)
    l1 = []
    for i in range(0, len(fqc)):
        for j in range(0, len(fqc[i])):
            l1.append(float(fqc[i][j]))
    return l1


def musical_notes(l1):
    """
    This function print the musical notes and its octave based in a turning frequency.
    :param l1:
    :return:
    """
    note, notes2, frequencias, l2, l3 = [], [], [], [], []
    for k in range(0, 101):
        la, q, cont = 27.5, 2, 12
        lg = 1 + log2(2 ** ((k + 1) / 12))
        f = round((la * q ** (lg - 1)), 1)
        frequencias.append(f)  # The list of all frequency in the piano.
    for i in range(0, len(l1)):  # theses iterations turning the instrument.
        menor, idx = 999999, 0
        for j in range(0, len(frequencias)):
            menos = abs(frequencias[j] - l1[i])
            if menos < menor:
                menor = menos
                idx = j
        l2.append(idx)
    for i in range(0, len(l2)):
        l3.append(frequencias[l2[i]])
    for k in range(0, len(frequencias)):
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        for i in range(0, len(l3)):  # Iterations in the list with frequencys.
            n = frequencias.index(l3[i]) - 2
            octv = k // 12
            while n >= 12:
                n -= 12
                octv += 1  # find the notes and octaves.
            note.append(notes[n] + str(octv + 1))  # The list of notes and its octaves.
        notes2.append(note)
        break
    for k in range(0, len(notes2)):
        for i in range(0, len(notes2[k])):
            if i >= len(notes2[k]) - 1:
                print(notes2[k][i])
                break
            print(notes2[k][i], end=" ")


musical_notes(frequency_of_notes())
