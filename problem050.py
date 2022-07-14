"""
===========
Palindromes
===========

The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.
Here are few examples:

Stats
Amore, Roma
No 'x' in Nixon
Was it a cat I saw?
As you see, case of the letters is ignored. Spaces and punctuations are ignored too.

Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.

Input data contains number of phrases in the first line.
Next lines contain one phrase each.
Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.

Example:

input data:
3
Stars
O, a kak Uwakov lil vo kawu kakao!
Some men interpret nine memos

answer:
N Y Y
"""

print('')
phrases = ['A, mi Iwpy-se, Nnes-Yp W Ii, ma',
           'H-amegi, diio, igfi, Pu Riallkai, Akllairu-P, ifgioiidi ge, Mah',
           'Fadpujef Iyn-ptdu-G yau h-Uaygudtpnyiejupdaf',
           'Rwgbya U, Kzyoo ue-A Tyj uw C, iejjeicw u jytaeuooyzkuy Bgwr',
           'Iykoaokelkhtzoii, xnyq Ynxi, io, Z thklecK o-A-oky i',
           'D-gyeyheoili, oehye ygd',
           'A-wbbye-E, Abeiiebaeeybb wa',
           'Kdzq-mcosoou, pyrvfpuuhyisl-s-Iyhuu pfvry, puoosocm qzdk',
           'Oz, Ia, yb-hioeldd leo, Ihy-Ya iz, o',
           'F euuaz, pymayi Mwp h Pwmiy, amypzauuef',
           'Akd Joj, Kirya, Zhhza-Yri-kjojdka',
           'Y U Dxu mqy, Ugiig, unqmuxd u-Y',
           'Odtafs-J Vcei, Aoz-moy yorzoaiecvjsf At, do',
           'Feeb ulcrbcev, ea tggtaeve Cbrc-Luree, F',
           'Jeeeeaopuchs-knuoyuyae ayuyounkshcupoaieeej',
           'Sgogauosiu ag ogs',
           'Rrh, aeizc C zieahrr']
n = 0
i = 0
v = []
while n < len(phrases):
    phrases[i] = phrases[i].upper()
    phrases[i] = phrases[i].replace(',', '')
    phrases[i] = phrases[i].replace('-', '')
    phrases[i] = phrases[i].replace(' ', '')
    v.append(phrases[i])
    i += 1
    n += 1
for i in range(0, len(v)):
    if v[i] == v[i][::-1]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
print('')
