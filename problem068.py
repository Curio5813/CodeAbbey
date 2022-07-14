"""
============
Bicycle Race
============

Two bicyclist start moving from different cities heading to meet each other somewhere in the middle
(not exactly since they travel with different speed).

The road is laid in straight line between two cities.

You will be given the distance between cities S (in kilometers) and speed values for two bicyclists
(A and B in kilometers per hour). Your task is to find their meeting point (its distance from the first
of cities).

Input data will have the number of test-cases in the first line.
Next lines will contain three values each S A B.
Answer should contain the distances between first city and rendezvous point (i.e. distance travelled by first
cyclist before they meet), separated with spaces.

Example:

input data:
2
10 1 1
20 1 2

answer:
5 6.66666667
Note: the floating point values should have precision 10e-7 or better
"""
print('')


def bicycle_race():
    encontros, contornos = [], ''
    dados = [435, 23, 29,
             220, 16, 10,
             21, 13, 23,
             204, 12, 20,
             23, 19, 15,
             224, 17, 11,
             24, 24, 28,
             16, 25, 29,
             104, 28, 22,
             58, 22, 30,
             200, 23, 19,
             98, 30, 28,
             32, 12, 11,
             20, 13, 22,
             15, 19, 14,
             58, 13, 18,
             12, 10, 18,
             24, 18, 29,
             10, 18, 29,
             103, 27, 11,
             245, 13, 11,
             27, 23, 21,
             10, 26, 27,
             31, 15, 28,
             154, 15, 13,
             339, 12, 16,
             130, 15, 18,
             40, 20, 23,
             14, 25, 19]
    for k in range(0, len(dados), 3):
        instante_encontro = dados[k] / (dados[k + 1] + dados[k + 2])
        distancia_percorrida = round(dados[k + 1] * instante_encontro, 8)
        if distancia_percorrida == int(distancia_percorrida):
            encontros.append(int(distancia_percorrida))
        else:
            encontros.append(distancia_percorrida)
    return f'{[m for m in encontros]}'.replace('[', '').replace(']', '').replace(',', '')


print(bicycle_race())
