"""
=================
Sort with Indexes
=================

After solving the task Bubble Sort we are supposed to learn about sorting arrays. Now we have a bit more
complicated programming problem for you, since it is important to have practice in sorting and handling
not only primitive values but also more complex objects.

As previously, we are given an array of numbers. It should be sorted first (in non-decreasing order) - and
then for each value its initial index should be printed (indexes start from 1).

I.e., suppose we have an array 50 98 17 79 which after sorting becomes 17 50 79 98. Now:

17 was at 3-rd place initially
50 was at 1-st place initially
79 was at 4-th place initially
98 was at 2-nd place initially

so result is
3 1 4 2

Initial data will contain array size at first line and array values itself in the second (integers separated
by spaces).
Answer should contain initial indexes of the array members after they are reordered by sorting.

Example:

input data:
4
50 98 17 79

answer:
3 1 4 2
"""

print('')
v1 = [730, 345, 57, 683, 630, 776, 405, 826, 489, 537, 579, 245, 448, 305, 103, 157, 197]
v2 = []
for i in range(1, len(v1) + 1):
    v2.append(i)
for i in range(0, len(v1)):
    if i >= len(v1) - 1:
        break
    if v1[i] > v1[i + 1]:
        while v1[i] > v1[i + 1] and i >= 0:
            v1.insert(i, v1[i + 1])
            v1.pop(i + 2)
            v2.insert(i, v2[i + 1])
            v2.pop(i + 2)
            i -= 1
for j in range(0, len(v2)):
    print(f'{v2[j]}', end=' ')
print('')
print('')
