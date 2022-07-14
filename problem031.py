"""
=============
Rotate String
=============

To rotate string by K characters means to cut these characters from the beginning and transfer them to
the end. If K is negative, characters, on contrary should be transferred from the end to the beginning.

Input data will contain the number of test-cases in the first line.
Following lines will contain number K and some string S separated by space - one pair in each line.
String S will contain only lowercase latin letters. K will not exceed half the length of S by absolute
value.
Answer should contain strings rotated in accordance with the rule above, separated by spaces.
For example:

input data:
2
3 forwhomthebelltolls
-6 verycomplexnumber

answer:
whomthebelltollsfor numberverycomplex

The task could be easily solved by creating new instance of string concatenating two substrings.
However, if you want more serious challenge, you are encouraged to perform rotation "in-place",
moving bytes of original string (i.e. without allocating memory for new instance). This could be
done with the help of a loop and only one temporary variable.
"""

v1 = [1, 'csgxplbunsiienxueafwtgrgm',
      3, 'lihoqnfyygugyeewro',
      1, 'qnkwiqcbolmmtaeaaezhza',
      -1, 'wqabhxrubhsskuaw',
      -4, 'olkuidebdeyioqjuxa',
      -3, 'witasuxtcaonklv',
      3, 'stwaphemieajgriasaojnr',
      -5, 'thucwlukcpajtghybrisayfuh',
      6, 'xyylhmoixcjarddfkleleoi']
v2 = []
for i in range(0, len(v1), 2):
    if v1[i] > 0:
        str1 = v1[i + 1]
        str2 = v1[i + 1][:v1[i]]
        str3 = v1[i + 1][v1[i]:] + str2
        v2.append(str3)
    if v1[i] < 0:
        str1 = v1[i + 1]
        str2 = v1[i + 1][v1[i]:]
        str3 = str2 + v1[i + 1][:v1[i]]
        v2.append(str3)
for k in range(0, len(v2)):
    print(v2[k], end=' ')
print('')
print('')
