def main():
    from csv import reader
    """
    If you solved the task about Neumann's Random Generator you are already aware
    that not all methods of generating pseudo-random sequences are good. Particularly,
    Neumann's method is not suitable for anything except programming exercises.

    Here is the other method which is more widespread (it is implemented in most of
    programming languages and libraries) and still simple enough: let us start with
    some initial number and generate each new member Xnext of a sequence by the current
    Xcur using the following rule:

    Xnext = (A * Xcur + C) % M

    So we need three constants to define such a sequence (and an initial number). Not
    all combinations of constants are good (you may read details at Random Numbers),
    however, here are many good variants which allow to produce sequences with period
    of M, i.e. significantly long.

    In this task we are going to build this algorithm to tell the value of n-th member
    of a sequence.

    Input data will contain the number of test-cases in the first line.
    Then test-cases will follow, each in separate line.
    Test-case consists of five values: A, C, M, X0, N where first three are the same as
    in formula, while X0 is the initial member of a sequence and N is the number of a
    member which we want to calculate.

    Answer should contain N-th member's value for each test-case, separated by spaces.

    Example:

    input data:
    2
    3 7 12 1 2
    2 3 15 8 10

    answer:
    1 11
    """
    v_temp, v_current, v_next, x_next = [], [], [], 0
    with open('linear_congruential_generator.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        v = [row for row in reader_csv]
    for k in range(0, len(v)):
        for i in range(0, len(v[k])):
            v_temp.append(int(v[k][i]))
        v_current.append(v_temp)
        v_temp = []
    for k in range(0, len(v_current)):
        n = 0
        while n < v_current[k][4]:
            x_next = (v_current[k][0] * v_current[k][3] + v_current[k][1]) % v_current[k][2]
            v_current[k][3] = x_next
            n += 1
        v_next.append(x_next)
    print(*v_next)


if __name__ == '__main__':
    main()
