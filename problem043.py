"""
============
Dice Rolling
============

When programming board or role-playing games, many novice programmers experience troubles in converting
random values to specific dice points. The goal of this task is to give a practice in simulation of dice
rolling by the values coming from a random numbers generator.

Suppose, we have generator which gives random values in range from 0 (inclusive) to 1 (not inclusive) - this
could be encountered in languages like Basic, Java, Matlab etc.

We want to convert these values with floating point to one of six integer numbers: from 1 to 6. This could be
achieved by the following steps:

Multiply random value by N which is the number of distinct values we want to get - in our case we multiply
by 6 and so result would be floating point value in range from 0 (inclusive) to 6 (not inclusive)
Now let us take the integer part of this result (calling function like floor or converting to int) - the
value will become one of 0, 1, 2, 3, 4, 5 with equal probability.
Since we need values from 1 to 6 let us simply add 1 to the result.
Now you'll be given several numbers in the range [0 .. 1) (be sure, they are provided by random number
generator) - and you are to convert them to dice points by applying the algorithm above.

Input data will contain the amount of values to convert in the first line.
Other lines will contain one value each, in form like 0.142857.
Answer should contain numbers from 1 to 6 for each of input values, produced by the discussed algorithm.

Example:

6
0.59558786964
0.861037873663
0.385597702116
0.246237673331
0.808033385314
0.0544673665427

answer:
4 6 3 2 5 1
"""

v1 = [0.626993691549,
      0.809225958772,
      0.906577636022,
      0.352780388668,
      0.0220190640539,
      0.0340747190639,
      0.170856167562,
      0.24622069858,
      0.571556633804,
      0.763557085302,
      0.209888124373,
      0.737089823931,
      0.930602953304,
      0.33224227326,
      0.0442676283419,
      0.33793518506,
      0.824120009318,
      0.907626349013,
      0.566867051646,
      0.370450318325,
      0.201418211684,
      0.294706174638,
      0.0111375357956,
      0.858344139531,
      0.206161170732,
      0.300057388376,
      0.43399770325,
      0.00552660413086,
      0.3551040194,
      0.176836350467]
v2 = []
for i in range(0, len(v1)):
    inteiro = (v1[i] * 6) // 1
    numero_dado = inteiro + 1
    v2.append(numero_dado)
for k in range(0, len(v2)):
    print(f'{v2[k]:.0f}', end=' ')
print('')
print('')
