"""
==============
Selection Sort
==============

Probably you've already solved the task of selecting minimum/maximum from array - this algorithm is based upon it.

Suppose we have an array of N values and want to sort them, just like in Bubble Sort:

[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

Let us work in the following manner:

over the whole array find the position of the maximum element (5 in the case above - 0-based index of value 9);
swap this element with the last one (because in the sorted array it should be the last, of course) - i.e. with
position N-1;

now regard the sub-array of length N-1, without the last value (which is already "in right place");
find the position of maximum element in this sub-array (i.e. second to maximum in the whole array) - now it would
be index 7 (where the value 6 resides);
swap it with the last element in the sub-array (i.e. with position N-2);
now regard the sub-array of the length N-2 (without two last elements) - do the following selection and swap and
so on;
algorithm ends when "sub-array" decreases to the length of 1.
Let us see an example step by step:

[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]      - max is 9 at position 5, swap 5-th with 9-th
[3, 1, 4, 1, 5, 3, 2, 6, 5], 9      - max is 6 at position 7, swap 7-th with 8-th
[3, 1, 4, 1, 5, 3, 2, 5], 6, 9      - max is 5 at position 4, swap 4-th with 7-th - they are equal!
[3, 1, 4, 1, 5, 3, 2], 5, 6, 9      - max is 5 at position 4, swap 4-th with 6-th
[3, 1, 4, 1, 2, 3], 5, 5, 6, 9      - max is 4 at position 2, swap 2-th with 5-th
[3, 1, 3, 1, 2], 4, 5, 5, 6, 9
...
[1], 1, 2, 3, 3, 4, 5, 5, 6, 9      - subarray of length 1 is reached, stop an algorithm.

Analysis
This algorithm needs to make about N passes through array and on each pass it performs about N/2 operations at
average, so it has O(N^2) "time complexity", the same as for Bubble Sort. However, unlike bubble sort it does
not perform about N/2 swaps on each pass - only a single swap is needed. This makes it work significantly faster,
though for large datasets more cunning algorithms are required.

One may select minimums instead of maximums and swap them with beginning of the array instead. Also, depending on
whether we select leftmost or rightmost maximum (or minimum) the sort could be either stable or unstable - meaning
that it either preserve or not the order of equal elements (which could be important when we sort objects, not
numbers.

You may read more in the topic on sorting algorithms comparison

Problem Statement
You are to implement the algorithm described above and print out the index of selected maximum at each pass.

Input data will contain N - the size of array - in the first line.
Next line will contain the array itself (all elements will be different).
Answer should contain indices of the maximums at each pass (N-1 values).

Example:

input data:
6
31 41 59 26 53 58

answer:
2 2 2 1 0
Let's examine processing of this example again, depicting swaps with clumsy arrows:

[31 41 59 26 53 58]
        ^       ^       on pass1: 2nd is max and is swapped to 5th
        \_______/

[31 41 58 26 53] 59
        ^    ^          on pass2: 2nd is max (again) and is swapped to 4th
        \____/

[31 41 53 26] 58 59
        ^ ^             on pass3: 2nd is max (yet again) and is swapped to 3rd
        \_/

[31 41 26] 53 58 59
     ^ ^                on pass4: 1st is max and swapped to 2nd
     \_/

[31 26] 41 53 58 59
  ^ ^                   on pass5: 0th is max and swapped to 1st
  \_/

[26] 31 41 53 58 59     when only 0th element is "unsorted", array is really sorted!
"""
print('')


def selection_sort():
    indices = []
    with open('selection_sort.txt') as arquivo:
        dados = [int(x) for x in arquivo.readline().split(' ')]
    n = len(dados)
    while n > 1:
        d = max(dados)
        indices.append(dados.index(d))
        dados.insert(dados.index(max(dados)), dados[-1])
        dados.pop()
        dados.pop(dados.index(max(dados)))
        n = len(dados)
    return f'{[k for k in indices]}'.replace('[', '').replace(']', '').replace(',', '')


print(selection_sort())
