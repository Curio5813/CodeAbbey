"""
==============
Parity Control
==============

Anna lives at Algol and Bob lives at Betelgeuse. Long distance separates them since these stars are in different
constellations - Perseus and Orion.

They found a way to communicate via e-mail. However, due to big distance, some letters could be changed during
transmission. Simple form of error-checking is proposed by Anna:

All letters are transmitted in usual ASCII code, one byte per symbol. Each byte consists of 8 bits, but the highest
bit is not used for English language - it is normally always 0.

Let us set this bit to either 0 or 1 in order that sum of bits in the whole byte is always even (2, 4, 6 or 8).
That is how some letters are encoded:

symbol     ascii-code     binary     num-of-bits    encoded-binary   encoded-dec

 'A'           65        01000001         2            01000001           65
 'B'           66        01000010         2            01000010           66
 'C'           67        01000011         3            11000011          195
 '.'           46        00101110         4            00101110           46
 ' '           32        00100000         1            10100000          160

It is supposed that communication line could not change more than one bit in each of the transmitted bytes. So the
bytes which have odd amount of bits are considered corrupted.

We are given the message in this protected encoding. Our task is to check each letter and remove those which are
corrupted. Others should be converted to normal ASCII and printed as characters.

Input data will contain bytes of the message transmitted (represented by the sequence of decimal values, separated
with spaces).
Original message consists only of latin letters (small and capital), digits and spaces.
The end of message is signalled by dot character '.' - you can assume this will never be corrupted.
Answer should contain message with corrupted bytes removed, highest bits cleared - and represented as characters
rather than numbers.

Example:

input data:
65 238 236 225 46

answer:
Ana.

"""

print('')
ascii_decimal = [32, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
                 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
characters = [' ', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c',
              'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
              'x', 'y', 'z']
letter = [195, 161, 237, 124, 216, 98, 195, 97, 209, 70, 195, 74, 113, 85, 109, 181, 232, 160, 231, 235, 247, 143,
          246, 122, 145, 54, 117, 231, 195, 108, 116, 243, 245, 111, 237, 101, 236, 240, 72, 235, 99, 77, 51, 181,
          53, 65, 119, 103, 72, 238, 180, 168, 177, 195, 90, 72, 212, 50, 119, 160, 233, 183, 66, 245, 206, 241,
          241, 199, 220, 66, 118, 65, 103, 99, 77, 112, 217, 177, 207, 80, 249, 227, 101, 122, 114, 148, 216, 180,
          112, 112, 240, 112, 191, 168, 181, 14, 168, 103, 216, 176, 46]
cont = 1
n = 128
soma = 0
a = 86
b = 0
v1 = []
v2 = []
v3 = []
for i in range(0, len(letter)):
    while soma != letter[i]:
        while soma < letter[i]:
            soma += n
            cont += 1
            n /= 2
        n *= 2
        cont -= 1
        while soma > letter[i]:
            soma -= n
        n /= 2
    soma = int(soma)
    v1.append(soma)
    v2.append(cont)
    soma = 0
    n = 128
    cont = 1
for i in range(0, len(v2)):
    n = 128
    if v2[i] % 2 == 0:
        if v1[i] in ascii_decimal:
            b = ascii_decimal.index(v1[i])
            c = characters[b]
            v3.append(c)
        else:
            if letter[i] > n:
                v1[i] -= n
                if v1[i] in ascii_decimal:
                    b = ascii_decimal.index(v1[i])
                    c = characters[b]
                    v3.append(c)
                while v1[i] not in ascii_decimal:
                    n /= 2
                    n = int(n)
                    v1[i] -= n
                    if v1[i] in ascii_decimal:
                        b = ascii_decimal.index(v1[i])
                        c = characters[b]
                        v3.append(c)
                    break
            while letter[i] < n:
                n /= 2
                n = int(n)
                v1[i] -= n
                if v1[i] in ascii_decimal:
                    b = ascii_decimal.index(v1[i])
                    c = characters[b]
                    v3.append(c)
                    break
                while v1[i] not in ascii_decimal:
                    n /= 2
                    n = int(n)
                    v1[i] -= n
                    if v1[i] in ascii_decimal:
                        b = ascii_decimal.index(v1[i])
                        c = characters[b]
                        v3.append(c)
                    break
for i in range(0, len(v3)):
    print(v3[i], end='')
print('')
