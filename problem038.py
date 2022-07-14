"""
==================
Quadratic Equation
==================

Now we are to create a program for solving quadratic equation. Supposedly you have learnt in school that
such equation has a form of:

A * x^2 + B * x + C = 0

where A, B and C are some constants (called "coefficients" of equation) and x is a variable. To solve such
equation means to find x for which the formula becomes true. For example with coefficients 3, -5 and -2 we
have equation:

3 * x^2 - 5 * x - 2 = 0

and we can see that value x = 2 is quite suitable.

General formula for finding such values (or "roots") via coefficients of equation is the following:

x1 = (-B + sqrt(B^2 - 4*A*C)) / (2*A)
x2 = (-B - sqrt(B^2 - 4*A*C)) / (2*A)

For example above these expressions will produce:

x1 = (5 + sqrt(5^2 + 4*3*2)) / (2*3) = (5 + 7) / 6 = 2
x2 = (5 - sqrt(5^2 + 4*3*2)) / (2*3) = (5 - 7) / 6 = -1/3

I.e. the equation really has two roots. Strictly speaking, here are always two roots. However, they could be:
- either distinct, when expression under sqrt is positive; - or equal, when expression under sqrt is zero;
- and in other cases even complex numbers - i.e. values like U+V*i where i = sqrt(-1).

Refer to wikipedia for more about Complex Numbers or Quadratic Equations at whole.

Input data will contain number of test-cases in the first line.
Each of test-cases will consist of three values (for A, B and C respectively).
Answer should contain a pair of roots for each case (even when they are equal). Use space to separate values
of the pair and use semicolon followed by space to separate pairs themselves. Complex numbers should be given
like 5-2i or -1+1i.

Note also:

order of values inside the pair is important - for real roots output the bigger one first; for complex roots
output a+bi first and a-bi last; roots would be always expressed with integer numbers in this task, so print
no any decimal points etc.

Example:

input data:
3
3 -3 -6
1 0 1
9 90 225

answer:
2 -1; 0+1i 0-1i; -5 -5
"""

from math import sqrt, gcd
print('')


def quadratic_equation():
    lista = [4, 56, 260,
             3, -12, -63,
             8, -160, 1448,
             6, -96, 378,
             4, -48, 128,
             2, -20, 32,
             2, -6, 0,
             3, -3, -18,
             2, -18, -20,
             2, 20, 250,
             5, -60, 200,
             1, 9, 8,
             3, 48, 267,
             8, -48, -216,
             6, -60, 54,
             8, 72, -80]
    for k in range(0, len(lista), 3):
        delta = lista[k + 1] ** 2 - 4 * lista[k] * lista[k + 2]
        if delta < 0:
            delta *= (-1)
            w = sqrt(delta)
            delta = int(w)
            if lista[k + 1] == 0:
                z = 2 * lista[k]
                t = lista[k + 1]
                u = delta
                mdc = gcd(u, z)
                u /= mdc
                z /= mdc
                if z > 1:
                    print(f'{round(t)}+{round(u)}i/{round(z)} {round(t)}-{round(u)}i/{round(z)};'.lstrip(";"), end=' ')
                if z == 1:
                    print(f'{round(t)}+{round(u)}i {round(t)}-{round(u)}i;'.lstrip(";"), end=' ')
            if lista[k + 1] == delta:
                z = 2 * lista[k]
                t = lista[k + 1]
                t *= -1
                u = delta
                mdc = gcd(t, z)
                t /= mdc
                u /= mdc
                z /= mdc
                if z > 1:
                    print(f'{round(t)}+{round(u)}i/{round(z)} {round(t)}-{round(u)}i/{round(z)};'.lstrip(";"), end=' ')
                if z == 1:
                    print(f'{round(t)}+{round(u)}i {round(t)}-{round(u)}i;'.lstrip(";"), end=' ')
            if lista[k + 1] < delta and lista[k + 1] != 0 and delta % lista[k + 1] == 0:
                z = 2 * lista[k]
                t = lista[k + 1]
                t *= -1
                u = delta
                mdc = gcd(t, z)
                t /= mdc
                u /= mdc
                z /= mdc
                if z > 1:
                    print(f'{round(t)}+{round(u)}i/{round(z)} {round(t)}-{round(u)}i/{round(z)};'.lstrip(";"), end=' ')
                if z == 1:
                    print(f'{round(t)}+{round(u)}i {round(t)}-{round(u)}i;'.lstrip(";"), end=' ')
            if lista[k + 1] > delta and lista[k + 1] % delta == 0:
                z = 2 * lista[k]
                t = lista[k + 1]
                t *= -1
                u = delta
                mdc = gcd(u, z)
                t /= mdc
                u /= mdc
                z /= mdc
                if z > 1:
                    print(f'{round(t)}+{round(u)}i/{round(z)} {round(t)}-{round(u)}i/{round(z)};'.lstrip(";"), end=' ')
                if z == 1:
                    print(f'{round(t)}+{round(u)}i {round(t)}-{round(u)}i;'.lstrip(";"), end=' ')
            if lista[k + 1] > delta and lista[k + 1] % delta != 0:
                z = 2 * lista[k]
                t = lista[k + 1]
                t *= -1
                u = delta
                mdc = gcd(u, z)
                t /= mdc
                u /= mdc
                z /= mdc
                if z > 1:
                    print(f'{round(t)}+{round(u)}i/{round(z)} {round(t)}-{round(u)}i/{round(z)};'.lstrip(";"), end=' ')
                if z == 1:
                    print(f'{round(t)}+{round(u)}i {round(t)}-{round(u)}i;'.lstrip(";"), end=' ')
            if lista[k + 1] < delta and lista[k + 1] != 0 and delta % lista[k + 1] != 0:
                z = 2 * lista[k]
                t = lista[k + 1]
                t *= -1
                u = delta
                mdc = gcd(t, z)
                t /= mdc
                u /= mdc
                z /= mdc
                if z > 1:
                    print(
                        f'{round(t)}+{round(u)}i/{round(z)} {round(t)}-{round(u)}i/{round(z)};'.lstrip(";"), end=' ')
                if z == 1:
                    print(f'{round(t)}+{round(u)}i {round(t)}-{round(u)}i;'.lstrip(";"), end=' ')
        else:
            y1 = int((-lista[k + 1] + sqrt(delta)))
            y2 = int((-lista[k + 1] - sqrt(delta)))
            z1 = (2 * lista[k])
            z2 = (2 * lista[k])
            mdc1 = gcd(y1, z1)
            mdc2 = gcd(y2, z2)
            y1 /= mdc1
            y2 /= mdc2
            z1 /= mdc1
            z2 /= mdc2
            if delta > 0:
                if z1 > 1 and z2 > 1:
                    print(f'{round(y1)}/{round(z2)} {round(y2)}/{round(z2)};'.lstrip(";"), end=' ')
                if z1 == 1 and z2 > 1:
                    print(f'{round(y1)} {round(y2)}/{round(z2)};'.lstrip(";"), end=' ')
                if z1 > 1 and z2 == 1:
                    print(f'{round(y1)}/{round(z2)} {round(y2)};'.lstrip(";"), end=' ')
                if z1 == 1 and z2 == 1:
                    print(f'{round(y1)} {round(y2)};'.lstrip(";"), end=' ')
            if delta == 0:
                if z1 > 1 and z2 > 1:
                    print(f'{round(y1)}/{round(z2)} {round(y2)}/{round(z2)};'.lstrip(";"), end=' ')
                if z1 == 1 and z2 > 1:
                    print(f'{round(y1)} {round(y2)}/{round(z2)};'.lstrip(";"), end=' ')
                if z1 > 1 and z2 == 1:
                    print(f'{round(y1)}/{round(z2)} {round(y2)};'.lstrip(";"), end=' ')
                if z1 == 1 and z2 == 1:
                    print(f'{round(y1)} {round(y2)};'.lstrip(";"), end=' ')
    return ''


print(quadratic_equation())
