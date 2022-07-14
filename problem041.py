"""
===============
Median of Three
===============

You probably already solved the problem Minimum of Three - and it was not great puzzle for you?
Since programmers should improve their logic (and not only skills in programming language), let us
change the task to make it more tricky.

You will be again given triplets of numbers, but now the middle of them should be chosen - i.e. not the
largest and not the smallest one. Such number is called the Median (of the set, array etc).

Be sure, this problem is not simply "another stupid exercise" - it is used as a part in powerful QuickSort
algorithm, for example.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected medians of triplets, separated by spaces.

Example:

data:
3
7 3 5
15 20 40
300 550 137

answer:
5 20 300

Note: if your program will have a lot of if-else-if-else statements, then you are probably doing
something wrong. Simple solution should have no more than three of them.
"""

print('')
v1 = [97, 177, 173,
      2, 25, 24,
      101, 107, 174,
      1085, 1006, 916,
      946, 868, 945,
      9, 82, 24,
      90, 8, 59,
      1, 273, 9,
      41, 3, 50,
      338, 269, 335,
      10, 464, 459,
      59, 62, 952,
      3, 52, 53,
      1052, 72, 6,
      123, 126, 205,
      103, 284, 100,
      150, 101, 53,
      7, 155, 84,
      741, 1156, 1098,
      345, 66, 71,
      552, 456, 67,
      90, 87, 175,
      71, 175, 177]
v2 = []
v3 = []
v4 = []
for i in range(0, len(v1), 3):
    if v1[i + 1] < v1[i] < v1[i + 2] or v1[i + 2] < v1[i] < v1[i + 1]:
        v2.append(v1[i])
    if v1[i] < v1[i + 1] < v1[i + 2] or v1[i + 2] < v1[i + 1] < v1[i]:
        v2.append(v1[i + 1])
    if v1[i] < v1[i + 2] < v1[i + 1] or v1[i + 1] < v1[i + 2] < v1[i]:
        v2.append(v1[i + 2])
for j in range(0, len(v2)):
    print(v2[j], end=' ')
print('')
print('')
