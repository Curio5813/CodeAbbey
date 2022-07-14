def main():
    from csv import reader
    """
    When program deals with numbers which have fraction part we sometimes want to round such values
    to whole integer. We'll need this for programming some later problems (to make answers simpler,
    for example), so let us have the following dedicated exercise to learn this trick.

    There are several pairs of numbers. For each pair you are to divide first by second and return
    the result, rounded to the nearest integer.

    In cases, when result contains exactly 0.5 as a fraction part, value should be rounded up
    (i.e. by adding another 0.5). Note that for negative values "greater" means "closer to zero".
    Refer to the Wikipedia page on Rounding for more thorough explanations.

    In any further problems, when rounding is mentioned - just the same rounding algorithm is supposed
    (unless other is explicitly specified).

    Input data will give a number of test-cases in the first line.
    Next lines will contain one test-case (i.e. the pair of numbers) each.
    Answer should contain division-and-rounding results for each pair, separated with spaces

    Example:
        input data:
        3
        12 8
        11 -3
        400 5
        answer:
        2 -4 80
    """
    data, list1, list2, rounding, rounded = [], [], [], [], []
    with open('rounding.csv') as arquivo:
        leitor_csv = reader(arquivo, delimiter=' ')
        data = [row for row in leitor_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            list1.append(int(data[k][i]))
        list2.append(list1)
        list1 = []
    for k in range(0, len(list2)):
        for i in range(0, len(list2[k]), 2):
            rounding.append(list2[k][i] / list2[k][i + 1])
    for k in range(0, len(rounding)):
        if rounding[k] + 0.5 == int(rounding[k] + 0.5):
            rounded.append(round(rounding[k] + 0.5))
        else:
            rounded.append(round(rounding[k]))
    print(*rounded)


if __name__ == '__main__':
    main()
