"""
==============
Triangle Area
==============

Being able to calculate area of triangle is quite important since many more complex tasks are often easily
reduced to this (and we will use it too later).

One of the oldest known methods is Heron's Formula which takes as inputs the lengths of the triangle's sides.

In this problem you however is to write a program which uses X and Y coordinates of the triangle's vertices
instead. So you can use either this formula somehow or find another one.

Input data will contain the number of triangles to process.
Next lines will contain 6 values each, in order X1 Y1 X2 Y2 X3 Y3, describing three vertices of a triangle.
Answer should give areas of triangles separated by space (precision about 1e-7 is expected).

Example:

data:
3
1 3 9 5 6 0
1 0 0 1 10000 10000
7886 5954 9953 2425 6250 2108

answer:
17 9999.5 6861563
"""
print('')

from math import sqrt


def triangule_area():
    areas = []
    dados = [1546, 5989, 1086, 1349, 4306, 7806,
             7675, 9612, 8361, 2441, 5256, 314,
             7807, 2943, 9909, 2977, 1353, 1993,
             4667, 9468, 9714, 2537, 1608, 3382,
             4513, 6832, 3402, 5255, 121, 346,
             4658, 1667, 6335, 5744, 3016, 640,
             3549, 690, 252, 1910, 3131, 5507,
             2224, 937, 8450, 2133, 3913, 9802,
             4125, 8580, 9269, 3838, 1116, 876,
             7220, 5629, 7708, 622, 884, 7829,
             967, 5541, 9495, 7302, 1284, 2511,
             7941, 4833, 3200, 8192, 6743, 6330,
             3699, 8966, 7267, 2148, 1099, 1179,
             1949, 5223, 9758, 1218, 9061, 874,
             2094, 6281, 6502, 9801, 6902, 7385,
             7629, 7869, 2926, 7124, 5170, 4210,
             9635, 3110, 9043, 2834, 1302, 5785]
    for k in range(0, len(dados), 6):
        x1 = dados[k + 2] - dados[k]
        y1 = dados[k + 3] - dados[k + 1]
        x2 = dados[k + 4] - dados[k]
        y2 = dados[k + 5] - dados[k + 1]
        x3 = dados[k + 4] - dados[k + 2]
        y3 = dados[k + 5] - dados[k + 3]
        a = sqrt(x1 ** 2 + y1 ** 2)
        b = sqrt(x2 ** 2 + y2 ** 2)
        c = sqrt(x3 ** 2 + y3 ** 2)
        s = (a + b + c) / 2
        area = round(sqrt(s * (s - a) * (s - b) * (s - c)), 8)
        areas.append(area)
    return f'{[num for num in areas]}'.replace('[', '').replace(']', '').replace(',', '')


print(triangule_area())
