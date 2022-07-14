"""
==================
Savings Calculator
==================

Joel wants to buy a boat which costs $10000. However, he currently has only $1000. One of the ways to increase
money is to put them into bank account and wait. For example, if account is incresed by 8% each year:

year     money
  0       1000
  1       1080
  2       1166.4
  3       1259.71
  4       1360.48
  5       1469.31
  6       1586.85
    .....
 29       9316.82
 30      10062.16

then Joel can grow his money in 30 years. Moreover, if account is increased not annually but monthly (with the
same interest rate of 8% per year) then the sum will be collected in only 29 years! Quite funny :)

In this task you need to help Joel to calculate how many years he need to wait depending on given starting amount
of money S, required sum R and bank's interest rate P. At the end of each year account is increased and rounded down
to whole cents (as in example above).

Input data contain number of test-cases in the first line.
Each of the following lines contain three numbers S, R and P.
Answer should contain number of years to wait for each case, separated by spaces.

Example:

input data:
2
1000 10000 8
50 100 25

answer:
30 4
"""

print('')


def juros_compostos():
    dados = [50, 700, 25,
             100, 1200, 35,
             1000, 15000, 3,
             2500, 37500, 1,
             50, 900, 1,
             25, 300, 6,
             25, 475, 15,
             5000, 25000, 20,
             25, 125, 35,
             50, 250, 5,
             50, 750, 2,
             1000, 18000, 25,
             25, 375, 3,
             500, 7500, 8,
             1000, 15000, 2,
             250, 1500, 50,
             50, 1000, 3]
    for k in range(0, len(dados), 3):
        anos = 0
        while dados[k] < dados[k + 1]:
            anos += 1
            dados[k] *= 1 + (dados[k + 2] / 100)
            dados[k] = round(dados[k], 8)
            a = str(dados[k])
            b = a.split('.')
            c = b[0] + '.' + b[1][0:2]
            d = float(c)
            dados[k] = d
        print(anos, end=' ')
    return ''


print(juros_compostos())
