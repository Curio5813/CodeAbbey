"""
================
Collatz Sequence
================

This is one of the most mysterious math problems of the last century - both because its statement is extremely
simple - and because the proof is still unknown. However it offers good programming exercise for beginners.

Suppose we select some initial number X and then build the sequence of values by the following rules:

if X is even (i.e. X modulo 2 = 0) then
    Xnext = X / 2
else
    Xnext = 3 * X + 1

I.e. if X is odd, sequence grows - and if it is even, sequence decreases. For example, with X = 15 we have
sequence:

15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1
After the sequence reaches 1 it enters the loop 1 4 2 1 4 2 1....

The intrigue is in the fact that any starting number X gives the sequence which sooner or later reaches 1 -
however though this Collatz Conjecture was expressed in 1937, up to now no one could find a proof that it is
really so for any X or could not find a counterexample (i.e. number for which sequence did not end with 1 -
either entering some bigger loop or growing infinitely).

Your task is for given numbers to calculate how many steps are necessary to come to 1.

Input data contains number of test-cases in the first line.
Second line contains the test-cases - i.e. the values for which calculations should be performed.
Answer should contain the same amount of results, each of them being the count of steps for getting Collatz
Sequence to 1.

For example:

input data:
3
2 15 97

answer:
1 17 118
"""

print('')
v1 = [26, 36778, 48382, 26907, 272, 45152, 500, 173, 4227, 8644, 6203, 2329, 14, 3801, 46627, 14, 34, 8750, 41]
cont = 0
v2 = []
i = 0
while i < len(v1):
    while v1[i] != 1:
        if v1[i] % 2 == 0:
            v1[i] = v1[i] / 2
            cont += 1
        elif v1[i] % 2 != 0:
            v1[i] = v1[i] * 3 + 1
            cont += 1
    v2.append(cont)
    i += 1
    cont = 0
for i in range(0, len(v2)):
    print(v2[i], end=' ')
print('')
print('')
