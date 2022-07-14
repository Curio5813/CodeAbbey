"""
=========
Bit Count
=========

As you probably know, all values inside a computer are represented in binary system. In this simple task you
are to write a program which counts the number of non-zero bits in a given value.

We are using 32-bit integer values, so there should be from 0 to 32 non-zero bits.

Please note that unlike most languages Python pretends that numbers are infinite-length (this will not prevent
you from solving this task, though some of methods usable for other languages may not work as expected).

For example:

value             binary                count
  1   00000000000000000000000000000001      1
100   00000000000000000000000001100100      3
 -1   11111111111111111111111111111111     32
Input data will contain a number of values to process.
Next line will contain the values themselves, each in range -2 000 000 000 .. 2 000 000 000.
Answer should contain the counts of bits set to 1 for each of values, separated by spaces.

Example:

input data:
3
1 100 -1

answer:
1 3 32
"""
print('')


def bit_count():
    bits = []
    dado = [-4, -664, 81, 5, 13557687, -1662555, 1584242, 1670062, -145, 1, -16142, 800874, 11636, -1194, -7,
            -1810, -1332873763, -51734761, 74, 91, 186080, 1149711231, -3302437, 59, -795370, 130549187,
            114886533, -87164812, 128984886, 161557, -57, -570228965, 27, 501233557, -1721, 13, -879512,
            639773264, -24348, 11416, 14671561, 14, -1685570688, -154289911, 1, 187365, -147180080]
    for k in range(0, len(dado)):
        if dado[k] > 0:
            bits_total, n = 1, 32
            valor_binario = 2 ** n
            while dado[k] != valor_binario:
                while dado[k] < valor_binario:
                    n -= 1
                    valor_binario = 2 ** n
                    if dado[k] == valor_binario:
                        bits.append(bits_total)
                while dado[k] > valor_binario:
                    n -= 1
                    valor_binario += 2 ** n
                    bits_total += 1
                    while valor_binario > dado[k]:
                        bits_total -= 1
                        n -= 1
                        valor_binario -= 2 ** n
                        bits_total += 1
                    if dado[k] == valor_binario:
                        bits.append(bits_total)
        if dado[k] < 0:
            dado[k] = dado[k] * -1
            bits_total, n, a = 1, 32, 0
            valor_binario = 2 ** n
            while dado[k] != valor_binario:
                while dado[k] < valor_binario:
                    n -= 1
                    valor_binario = 2 ** n
                    if dado[k] == valor_binario:
                        bits_total = 1 + (32 - (n + 1)) - (bits_total - 1)
                        bits.append(bits_total)
                while dado[k] > valor_binario:
                    n -= 1
                    valor_binario += 2 ** n
                    bits_total += 1
                    while valor_binario > dado[k]:
                        bits_total -= 1
                        n -= 1
                        valor_binario -= 2 ** n
                        bits_total += 1
                    if dado[k] == valor_binario:
                        bits_total = 1 + (32 - (n + 1)) - (bits_total - 1)
                        bits.append(bits_total)
    return f'{[num for num in bits]}'.replace('[', '').replace(']', '').replace(',', '')


print(bit_count())
