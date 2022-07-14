def main():
    from csv import reader
    """
    Very common problem in computational programming is to determine the underlying law to which some
    phenomenon obeys. For learning purpose let us practice a simple variant - discovering linear
    dependence by two given observations (for example, how the price for some product depends on
    its size, weight etc.)

    Linear function is defined by an equation:

    y(x) = ax + b
    Where a and b are some constants.
    For example, with a=3, b=2 function will yield values y = 2, 5, 8, 11...
    for x = 0, 1, 2, 3...

    Your task is to determine a and b by two points, belonging to the function.
    I.e. you are told two pairs of values (x1, y1), (x2, y2) which satisfy the function equation -
    and you should restore the equation itself.

    Input data have the number of test-cases in the first line
    and then test-cases themselves in separate lines.
    Each case contains 4 integers (x1 y1 x2 y2).
    Answers should be integer too and you are to write them in line, separating with spaces and
    enclosing each pair in parenthesis, for example:

    input data:
    2
    0 0 1 1
    1 0 0 1
    answer:
    (1 0) (-1 1)
    """
    l1, l2 = [], []
    with open('linear_function.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        data = [row for row in reader_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            l1.append(int(data[k][i]))
        l2.append(l1)
        l1 = []
    for k in range(0, len(l2)):
        a = round((l2[k][1] - l2[k][3]) / (l2[k][0] - l2[k][2]))
        b = round((l2[k][1]) - a * (l2[k][0]))
        print(f'({a} {b})', end=' ')


if __name__ == '__main__':
    main()
