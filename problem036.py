"""
============
Code Guesser
============

If you know the old game Bulls and Cows, this programming problem will look familiar to you.

Andrew and Peter play the code-guessing game. Andrew chooses a secret number consisting of 3 digits. Peter
tries to guess it, proposing several values, one by one.

For each guess Andrew should answer how many digits are correct - i.e. are the same in the proposed value and
in his secret number - and are placed in the same position. For example, if secret number is 125 and Peter calls
523, then Andrew answers with 1. Here is the sample of the game:

Andrew chooses a secret number 846

Peter's guess             Andrew's answer
      402                        0
      390                        0
      816                        2
      848                        2
      777                        0
      815                        1
      846                        3

So Peter have guessed correct number after 6 attempts.

You are to write program which reads guesses given by Peter (except the last) and prints out the secret number
choosen by Andrew. It is guaranteed that exactly one solution exists.

Input data will contain number of guesses in the first line.
Then answers with attempts will follow - each contains the number told by Peter and the answer given by Andrew.
In contrast with examples numbers will be of 4 digits.
Answer should contain the secret number (also 4 digits). See example:

input data:
6
402 0
390 0
816 2
848 2
777 0
815 1

answer:
846
Here we use 3-digit values for brevity, but the algorithm is the same.
"""
print('')


def code_guesser():
    texto, dados = '', []
    wrong0, wrong1, wrong2, wrong3 = [], [], [], []
    doubt0, doubt1, doubt2, doubt3 = [], [], [], []
    lessdoubt0, lessdoubt1, lessdoubt2, lessdoubt3 = [], [], [], []
    veryclue0, veryclue1, veryclue2, veryclue3 = [], [], [], []
    clue0, clue1, clue2, clue3 = [], [], [], []
    n = 0
    sure0, sure1, sure2, sure3 = [], [], [], []
    sure, answer = [], []
    with open('code_guesser.txt') as arquivo:
        lista = list(arquivo)
    for k in range(0, len(lista)):
        texto += lista[k]
        texto = texto.replace('\n', '')
        dados.append(texto.split(' '))
        texto = ''
    for k in range(0, len(dados)):
        if dados[k][1] == '0':
            wrong0.append(dados[k][0][0])
            wrong1.append(dados[k][0][1])
            wrong2.append(dados[k][0][2])
            wrong3.append(dados[k][0][3])
        if dados[k][1] == '1':
            doubt0.append(dados[k][0][0])
            doubt1.append(dados[k][0][1])
            doubt2.append(dados[k][0][2])
            doubt3.append(dados[k][0][3])
        if dados[k][1] == '2':
            lessdoubt0.append(dados[k][0][0])
            lessdoubt1.append(dados[k][0][1])
            lessdoubt2.append(dados[k][0][2])
            lessdoubt3.append(dados[k][0][3])
    while n < len(doubt0):
        if doubt0[n] not in wrong0:
            clue0.append(doubt0[n])
        elif doubt0[n] in wrong0:
            clue0.append('x')
        if doubt1[n] not in wrong1:
            clue1.append(doubt1[n])
        elif doubt1[n] in wrong1:
            clue1.append('x')
        if doubt2[n] not in wrong2:
            clue2.append(doubt2[n])
        elif doubt2[n] in wrong2:
            clue2.append('x')
        if doubt3[n] not in wrong3:
            clue3.append(doubt3[n])
        elif doubt3[n] in wrong3:
            clue3.append('x')
        n += 1
    print(wrong0)
    print(wrong1)
    print(wrong2)
    print(wrong3)
    print('')
    print(doubt0)
    print(doubt1)
    print(doubt2)
    print(doubt3)
    print('')
    print(clue0)
    print(clue1)
    print(clue2)
    print(clue3)
    n = -1
    while n >= -len(clue0):
        if clue0[n] != 'x' and clue1[n] == 'x' and clue2[n] == 'x' and clue3[n] == 'x':
            sure0.append(clue0[n])
            break
        n -= 1
    n = -1
    while n >= - len(clue1):
        if clue1[n] != 'x' and clue0[n] == 'x' and clue2[n] == 'x' and clue3[n] == 'x':
            sure1.append(clue1[n])
            break
        n -= 1
    n = -1
    while n >= - len(clue2):
        if clue2[n] != 'x' and clue0[n] == 'x' and clue1[n] == 'x' and clue3[n] == 'x':
            sure2.append(clue2[n])
            break
        n -= 1
    n = -1
    while n >= -len(clue3):
        if clue3[n] != 'x' and clue0[n] == 'x' and clue1[n] == 'x' and clue2[n] == 'x':
            sure3.append(clue3[n])
            break
        n -= 1
    while len(sure0) == 0 and len(sure1) == 0 and len(sure2) == 0 and len(sure3) == 0:
        n = -1
        if len(sure0) > 0:
            while n > -len(clue0):
                if clue0[n] != sure0[0]:
                    if clue1[n] != 'x' and clue2[n] == 'x' and clue3[n] == 'x':
                        if len(sure1) == 0:
                            sure1.append(clue1[n])
                    if clue2[n] != 'x' and clue1[n] == 'x' and clue3[n] == 'x':
                        if len(sure2) == 0:
                            sure2.append(clue2[n])
                    if clue3[n] != 'x' and clue1[n] == 'x' and clue2[n] == 'x':
                        if len(sure3) == 0:
                            sure3.append(clue3[n])
                n -= 1
        n = -1
        if len(sure1) > 0:
            while n > -len(clue1):
                if clue1[n] != sure1[0]:
                    if clue0[n] != 'x' and clue2[n] == 'x' and clue3[n] == 'x':
                        if len(sure0) == 0:
                            sure0.append(clue0[n])
                    if clue2[n] != 'x' and clue0[n] == 'x' and clue3[n] == 'x':
                        if len(sure2) == 0:
                            sure2.append(clue2[n])
                    if clue3[n] != 'x' and clue0[n] == 'x' and clue2[n] == 'x':
                        if len(sure3) == 0:
                            sure3.append(clue3[n])
                n -= 1
        n = -1
        if len(sure2) > 0:
            while n > -len(clue2):
                if clue2[n] != sure2[0]:
                    if clue0[n] != 'x' and clue1[n] == 'x' and clue3[n] == 'x':
                        if len(sure0) == 0:
                            sure0.append(clue0[n])
                    if clue1[n] != 'x' and clue0[n] == 'x' and clue3[n] == 'x':
                        if len(sure1) == 0:
                            sure1.append(clue1[n])
                    if clue3[n] != 'x' and clue0[n] == 'x' and clue1[n] == 'x':
                        if len(sure3) == 0:
                            sure3.append(clue3[n])
                n -= 1
        n = -1
        if len(sure3) > 0:
            while n > -len(clue3):
                if clue3[n] != sure3[0]:
                    if clue0[n] != 'x' and clue1[n] == 'x' and clue2[n] == 'x':
                        if len(sure0) == 0:
                            sure0.append(clue0[n])
                    if clue1[n] != 'x' and clue0[n] == 'x' and clue2[n] == 'x':
                        if len(sure1) == 0:
                            sure1.append(clue1[n])
                    if clue2[n] != 'x' and clue0[n] == 'x' and clue1[n] == 'x':
                        if len(sure2) == 0:
                            sure2.append(clue2[n])
                n -= 1
    sure.append(sure0[0])
    sure.append(sure1[0])
    sure.append(sure2[0])
    sure.append(sure3[0])
    n = 0
    while n < len(sure):
        texto += sure[n]
        n += 1
    answer.append(int(texto))
    print(*answer)


code_guesser()
