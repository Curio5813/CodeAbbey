def main():
    from csv import reader
    """
    When we speak about arithmetic progression (or arithmetic sequence) we mean a series of
    numbers with a special
    property - each value is followed by the other, greater by predefined amount (step).

    I.e. difference of (K+1)-th and K-th values is a constant. Here are examples of sequences

    1 2 3 4 5 6 7 ...
    4 6 8 10 12 14 16...
    10 13 16 19 22 25 28...

    Since so, arithmetic sequence is completely defined by the first member (A) and the increment value -
    step size - (B).
    First few members could be expressed as:

    A + (A + B) + (A + 2B) + (A + 3B) + ...

    You are to calculate the sum of first members of arithmetic sequence. Wikipedia page on arithmetic
    progression could
    be of significant help to one who meets them for the first time.

    Input data: first line contains the number of test-cases.
    Other lines contain test-cases in form of triplets of values A B N where A is the first value of
    the sequence, B is the step size and N is the number of first values which should be accounted.
    Answer: you are to output results (sums of N first members) for each sequence, separated by spaces.

    Example:

    data:
    2
    5 2 3
    3 0 10
    answer:
    21 30

    Explanation of the Example. In the first case we have sequence starting with 5 and increasing by
    2 each time. We want to sum 3 elements from it 5 + 7 + 9 = 21. The second is easier. It
    starts with 3 but increment is 0, so it is 3 + 3 + ... + 3 = 30 (total of 10 elements).

    Soma = n * (a1 + an) / 2
    """
    l1, l2, last, somas = [], [], 0, []
    with open('arithmetic_progression.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        data = [row for row in reader_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            l1.append(int(data[k][i]))
        l2.append(l1)
        l1 = []
    for k in range(0, len(l2)):
        last = l2[k][0] + ((l2[k][1]) * (l2[k][2] - 1))
        somas.append(round((l2[k][2] * (l2[k][0] + last)) / 2))
    print(*somas)


if __name__ == '__main__':
    main()
