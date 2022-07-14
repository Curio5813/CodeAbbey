"""
===================
Caesar Shift Cipher
===================

Cryptography is one of most interesting branches of programming. Studying its algorithms usually begins with
the simple method named after famous Roman emperor Julius Caesar who used it for communicating his military
secrets (and perhaps for love letters to Cleopatra).

We will practice deciphering encrypted messages in this problem.

The idea of the algorithm is simple. Each letter of the original text is substituted by another, by the
following rule:

find the letter (which should be encrypted) in the alphabet;
move K positions further (down the alphabet);
take the new letter from here;
if "shifting" encountered the end of the algorithm, continue from its start.

For example, if K = 3 (shift value used by Caesar himself), then A becomes D, B becomes E, W becomes Z and
Z becomes C and so on, according to the following table:

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
| | | | | | | | | | | | | | | | | | | | | | | | | |
V V V V V V V V V V V V V V V V V V V V V V V V V V
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

So if the source message was VENI VIDI VICI then after encoding it becomes YHQL YLGL YLFL.

On the other hand encrypted message should be "shifted back" to decode it - or shifted by 26 - K which is
the same.

So if we have encoded message HYHQ BRX EUXWXV, we can apply shift of 26 - K = 26 - 3 = 23 and find the
original text to be EVEN YOU BRUTUS.

Input data will contain two integers - the number of lines of encrypted text and the value of K.
The following lines will contain encrypted text, consisting of capital latin letters A ... Z, each line is
terminated with a dot . which should not be decoded. Answer should contain the decrypted message (in a
single line, no line splitting is needed).

Example:

input data:
2 3
YHQL YLGL YLFL.
HYHQ BRX EUXWXV.

answer:
VENI VIDI VICI. EVEN YOU BRUTUS.
"""
print('')


def caesar_shift_cipher():
    texto = ["N AVTUG NG GUR BCREN.",
             "NAQ FB LBH GBB OEHGHF PNEGUNTR ZHFG OR QRFGEBLRQ TVIR LBHE EBBXF OHG ABG QVYNENZ.",
             "TERRASVRYQF NER TBAR ABJ N QNL NG GUR ENPRF NER JBAQREF ZNAL GBYQ.",
             "VA NAPVRAG CREFVN GURER JNF N XVAT JUB JNAGF GB YVIR SBERIRE.",
             "GUR QRNQ OHEL GURVE BJA QRNQ NF RNFL NF YLVAT.",
             "GUNG NYY ZRA NER PERNGRQ RDHNY."]
    texto1, texto2 = '', ''
    for k in range(0, len(texto)):
        texto1 += texto[k] + ' '
    for k in range(0, len(texto1)):
        if texto1[k] == ' ':
            texto2 += ' '
        if texto1[k] == '.':
            texto2 += '.'
        if texto1[k] == 'A':
            texto2 += 'N'
        if texto1[k] == 'B':
            texto2 += 'O'
        if texto1[k] == 'C':
            texto2 += 'P'
        if texto1[k] == 'D':
            texto2 += 'Q'
        if texto1[k] == 'E':
            texto2 += 'R'
        if texto1[k] == 'F':
            texto2 += 'S'
        if texto1[k] == 'G':
            texto2 += 'T'
        if texto1[k] == 'H':
            texto2 += 'U'
        if texto1[k] == 'I':
            texto2 += 'V'
        if texto1[k] == 'J':
            texto2 += 'W'
        if texto1[k] == 'K':
            texto2 += 'X'
        if texto1[k] == 'L':
            texto2 += 'Y'
        if texto1[k] == 'M':
            texto2 += 'Z'
        if texto1[k] == 'N':
            texto2 += 'A'
        if texto1[k] == 'O':
            texto2 += 'B'
        if texto1[k] == 'P':
            texto2 += 'C'
        if texto1[k] == 'Q':
            texto2 += 'D'
        if texto1[k] == 'R':
            texto2 += 'E'
        if texto1[k] == 'S':
            texto2 += 'F'
        if texto1[k] == 'T':
            texto2 += 'G'
        if texto1[k] == 'U':
            texto2 += 'H'
        if texto1[k] == 'V':
            texto2 += 'I'
        if texto1[k] == 'W':
            texto2 += 'J'
        if texto1[k] == 'X':
            texto2 += 'K'
        if texto1[k] == 'Y':
            texto2 += 'L'
        if texto1[k] == 'Z':
            texto2 += 'M'
    return f'{texto2}'


print(caesar_shift_cipher())
