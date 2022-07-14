"""
===================
Pythagorean Theorem
===================

Triangle is called right when one of its three angles is right angle, equal to 90° - i.e. sides of this
angle are orthogonal.

Such triangles are important since for them the Pythagorean Theorem works. Let's recollect it.

Sides, adjacent to the right angle of such triangle, are called legs and the third side is hypotenuse.
The theorem states that length of hypotenuse is determined by the lengths of legs with simple formula:

c^2 = a^2 + b^2

    or

c = sqrt(a^2 + b^2)

Where c is the length of hypotenuse, while a and b are lengths of legs.

Famous example of the right triangle is one with sides of 3, 4 and 5 units. Really, for them theorem holds:

5^2 = 3^2 + 4^2

    or

25 = 9 + 16

In this task you will use this theorem to write a program which could determine, whether the triangle is right,
or it is acute, or obtuse:

for acute triangle its longest side is shorter than hypotenuse should be;
for obtuse triangle its longest side is longer than hypotenuse should be.
Input data contains the number of triangles in the first line.
Next lines describe one triangle each. Descriptions consist of three values - lengths of sides.
Largest value would always be the last of three for simplicity.
Answers should have one of the letters R (right), A (acute) or O (obtuse) for each of triangles.
Letters should be separated by spaces.

Example:

input data:
3
6 8 9
9 12 15
16 12 22

answer:
A R O
"""

print('')
v = [176, 132, 208,
     24, 18, 30,
     12, 16, 20,
     165, 396, 400,
     455, 1560, 1608,
     2208, 644, 2210,
     372, 279, 465,
     1080, 450, 1214,
     497, 1704, 1775,
     155, 372, 418,
     600, 320, 675,
     136, 102, 184,
     164, 123, 205,
     212, 159, 229,
     240, 100, 258,
     399, 1368, 1375,
     750, 400, 850,
     96, 40, 102,
     672, 280, 697,
     553, 1896, 1975,
     1164, 485, 1338,
     352, 264, 440,
     1584, 462, 1712,
     2280, 665, 2375,
     924, 385, 970,
     12, 16, 23,
     528, 154, 550,
     408, 119, 431,
     185, 444, 481,
     368, 276, 529]


def determinating_triangules():
    triangules = []
    for k in range(0, len(v), 3):
        if v[k] ** 2 + v[k + 1] ** 2 == v[k + 2] ** 2:
            result = 'R'
            triangules.append(result)
        if v[k] ** 2 + v[k + 1] ** 2 > v[k + 2] ** 2:
            result = 'A'
            triangules.append(result)
        if v[k] ** 2 + v[k + 1] ** 2 < v[k + 2] ** 2:
            result = 'O'
            triangules.append(result)
    for k in range(0, len(triangules)):
        print(triangules[k], end=' ')
    return ''


print(determinating_triangules())
