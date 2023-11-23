from math import log2
from csv import reader


def frequency_of_notes():
    """
    This function return a list of frequency of all musical notes that
    is produced by piano.
    :return:
    """
    la, q, l1 = 27.5, 2, []
    for i in range(1, 90):
        lg = 1 + log2(2 ** ((i - 1) / 12))
        f = la * q ** (lg - 1)  # This formula above and in this row calculate the frequency
        l1.append(f)            # in the temperated music instruments.
    return l1


def musical_notes(l1):
    """
    This function print the musical note, its octave, and  your frequency.
    :param l1:
    :return:
    """
    note, answer1, answer2 = [], [], []
    for k in range(0, 101):
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        la, q, cont = 27.5, 2, 12
        lg = 1 + log2(2 ** ((k + 1) / 12))
        f = la * q ** (lg - 1)
        octv = (k // 12)  # This formula calculate the octave in piano's keyboard.
        if k < 2:
            octv = 0
        else:
            octv += 1
        for i in range(0, len(l1)):  # Iterations in the list with frequencys.
            if l1[i] % f == 0:
                n = l1.index(l1[i]) - 1
                if k > 2 and notes[n + cont][0] == 'A' or notes[n + cont][0] == 'B':
                    octv -= 1
                note.append(notes[n + cont] + str(octv))
                break
            if i % 12 == 0:
                cont -= 12
    arq = open("problem088.csv")
    notas = reader(arq, delimiter=" ")
    notas = list(*notas)
    for k in range(0, len(notas)):
        for i in range(0, len(note)):
            if notas[k] == note[i]:
                answer1.append(notas[k])
                answer2.append(round(l1[i]))
    print(*answer1)
    print(len(answer2))
    print(*answer2)


musical_notes(frequency_of_notes())
