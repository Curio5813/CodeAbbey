from csv import reader
from time import time


start = time()


def fibonacci_divisibility_advanced():
    """
    Given usual Fibonacci Sequence, starting with 0 and 1:

            0 1 1 2 3 5 8 13 21 34 ...

    and some value M you will be asked to find the index of the
    first non-zero member of this list, which is evenly divisible
    by this M, e.g. if you are given M = 17 the answer is 9 (the
    index of the element 34).

    Input data in the first line will contain the number of test-cases.
    Next line will contain exactly this of divisors M (not exceeding 2_000_000)
    for which you should give answers. Answer should contain indices of
    members of Fibonacci Sequence, separated by spaces.
    :return:
    """
    arq = open("problem071.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    for i in range(0, len(l1)):
        l1[i] = int(l1[i])
    a, b = 0, 1
    p = a + b
    l2 = []
    print(*l1)
    for i in range(0, len(l1)):
        a, b = 0, 1
        p = a + b
        for k in range(2_000_000 + 1):
            a, b = b, p
            p = a + b
            if a % l1[i] == 0:
                l2.append(k + 1)
                print(k + 1, end=" ")
                break
    print("\n")
    print(*l2)


fibonacci_divisibility_advanced()

end = time()
print(f"{(end - start):.2f} segs")
