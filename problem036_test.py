print('')
guess = ['2508', 0,
         '8673', 1,
         '3904', 0,
         '7218', 0,
         '0227', 0,
         '6535', 0,
         '0495', 0,
         '4677', 2,
         '1750', 0,
         '3236', 0,
         '1309', 0,
         '6176', 1,
         '4040', 2,
         '5856', 0,
         '2526', 0,
         '1943', 0,
         '6949', 0,
         '1753', 0,
         '1527', 0,
         '7941', 1]
answer, wrong_guessing = [], []
guessing, pos0, pos1, pos2, pos3 = [], [], [], [], []
guessed0, guessed1, guessed2, guessed3, wrong0, wrong1, wrong2, wrong3 = [], [], [], [], [], [], [], []
doubt0, doubt1, doubt2, doubt3, maybe0, maybe1, maybe2, maybe3 = [], [], [], [], [], [], [], []
for k in range(0, len(guess), 2):
    if guess[k + 1] > 0:
        guessing.append(guess[k + 1])
        pos3.append(guess[k][3])
        pos2.append(guess[k][2])
        pos1.append(guess[k][1])
        pos0.append(guess[k][0])
    if guess[k + 1] == 0:
        wrong_guessing.append(guess[k + 1])
        wrong3.append(guess[k][3])
        wrong2.append(guess[k][2])
        wrong1.append(guess[k][1])
        wrong0.append(guess[k][0])
print(guessing)
print('')
print(pos0)
print(pos1)
print(pos2)
print(pos3)
print('')
for k in range(0, len(pos0)):
    if pos0[k] not in wrong0:
        doubt0.append(pos0[k])
for k in range(0, len(pos1)):
    if pos1[k] not in wrong1:
        doubt1.append(pos1[k])
for k in range(0, len(pos2)):
    if pos2[k] not in wrong2:
        doubt2.append(pos2[k])
for k in range(0, len(pos3)):
    if pos3[k] not in wrong3:
        doubt3.append(pos3[k])
for k in range(0, len(pos0)):
    if k >= len(pos0) - 1:
        break
    if guessing[k] == 1:
        if pos0[k] == pos0[k + 1]:
            maybe0.append(pos0[k])
        if pos1[k] == pos1[k + 1]:
            maybe1.append(pos1[k])
        if pos2[k] == pos2[k + 1]:
            maybe2.append(pos2[k])
        if pos3[k] == pos3[k + 1]:
            maybe3.append(pos3[k])
    """
    if guessing[k] == 2:
        if pos0[k] == pos0[k + 1]:
            maybe0.append(pos0[k])
        if pos1[k] == pos1[k + 1]:
            maybe1.append(pos1[k])
        if pos2[k] == pos2[k + 1]:
            maybe2.append(pos2[k])
        if pos3[k] == pos3[k + 1]:
            maybe3.append(pos3[k])
    if guessing[k] == 3:
        if pos0[k] == pos0[k + 1]:
            maybe0.append(pos0[k])
        if pos1[k] == pos1[k + 1]:
            maybe1.append(pos1[k])
        if pos2[k] == pos2[k + 1]:
            maybe2.append(pos2[k])
        if pos3[k] == pos3[k + 1]:
            maybe3.append(pos3[k])
    """
print('')
print(maybe0)
print(maybe1)
print(maybe2)
print(maybe3)
print('')
print(doubt0)
print(doubt1)
print(doubt2)
print(doubt3)
print('')


# my answer: 6673
# answer: 4071