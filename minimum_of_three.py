def main():
    from csv import reader
    """
    Several triplets of numbers are given to you. Your task is to select minimum among each
    of triplets.

    Input data will contain in the first line the number of triplets to follow.
    Next lines will contain one triplet each.
    Answer should contain selected minimums of triplets, separated by spaces.

    data:
    3
    7 3 5
    15 20 40
    300 550 137
    answer:
    3 15 137
    """
    data, list1, list2, minimum = [], [], [], []
    with open('minimum_of_three.csv') as arquivo:
        leitor_csv = reader(arquivo, delimiter=' ')
        for row in leitor_csv:
            data.append(row)
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            list1.append(int(data[k][i]))
        list2.append(list1)
        minimum.append(min(list2[k]))
        list1 = []
    print(*minimum)


if __name__ == '__main__':
    main()
