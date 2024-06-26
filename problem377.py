from csv import reader


def sum_of_digits_divisibility():
    """
    Let's regard sum of digits for first few positive numbers, and remainders they give when divided by 10:

    value   sum-of-digits   SD % 10
      1           1            1
      2           2            2
                 ...
      9           9            9
     10           1            1
     11           2            2
                 ...
     18           9            9
     19          10            0
                 ...
     99          18            8
    100           1            1

    Thus the first sum-of-digits which is divisible by 10 is for number 19.
    The next is for number 28. It is a bit annoying that remainders do not
    follow exact order, you see after 99 remainder "jumps" from 8 to 1.

    We want to calculate for given K the k-th number for which sum of digits
    is divisible by 10.

    Input data: number T of the testcases to follow is in the first line.
    Next T lines contain single integer each - the value K.

    Answers should be given as usually, as T values separated with spaces.
    :return:
    """
    arq = open("probelm377.cvs")
    l1 = reader(arq)
    l1 = list(l1)
    l2, int_str = [], 0
    for i in range(0, len(l1)):
        l2.append(int(l1[i][0]))
    for i in range(1, 100000000000):
        str_sum = str(i)
        for k in str_sum:
            int_str += int(k)
        if int_str % 10 == 0:
            print(i)
            int_str = 0
        else:
            int_str = 0


sum_of_digits_divisibility()
