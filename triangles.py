def main():
    from csv import reader
    """
    Triangle is an object built of three line segments (sides of triangle), connected by ends.
    Wiki on triangles provides more detailed explanation.

    If we have three line segments with lengths A B C - we either can built a triangle with them
    (for example with 3 4 5 or 3 4 7 - though this is with zero area) or we found it impossible
    (for example 1 2 4).

    You are given several triplets of values representing lengths of the sides of triangles.
    You should tell from which triplets it is possible to build triangle and for which it is not.

    Input data: First line will contain number of triplets.
    Other lines will contain triplets themselves (each in separate line).
    Answer: You should output 1 or 0 for each triplet (1 if triangle could be built and 0 otherwise).

    Example:

    data:
    2
    3 4 5
    1 2 4
    answer:
    1 0
    """
    l1, l2, asw = [], [], []
    with open('triangles.csv') as arquivo:
        reder_csv = reader(arquivo, delimiter=' ')
        data = [row for row in reder_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            l1.append(int(data[k][i]))
        l2.append(l1)
        l1 = []
    for k in range(0, len(l2)):
        if l2[k][0] + l2[k][1] > l2[k][2] and l2[k][0] + l2[k][2] > l2[k][1] and l2[k][1] + l2[k][2] > l2[k][0]:
            asw.append(1)
        else:
            asw.append(0)
    print(*asw)


if __name__ == '__main__':
    main()
