from csv import reader


def number_of_steps_in_euclidean_algorithm():
    """
    In the Euclidean algorithm, two integers x and y with x>=y are
    replaced with y and x mod y until y becomes 0. For example:

    (x, y) = (9, 7) is replaced with (7, 2),
    which then is replaced with (2, 1),
    which then is replace with (1, 0), and the algorithm terminates.
    Overall, the algorithm took three steps.

    Your task is to find integer pairs for which the Euclidean algorithm
    runs exactly n steps.

    Input: The first line contains the number t of test cases.
    The second line contains t integer values – each is the count of
    target steps for the Euclidean algorithm.

    Output: A single line of t space-separated integer pairs x and y with
    x >= y >=1 so that the Euclidean algorithm for the i-th pair takes exactly
    the i-th target number of steps.
    :return:
    """
    arq = open("problem385.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    [int(l1[i]) for i in range(0, len(l1))]
    resto, step, steps = 0, 0, []
    for i in range(2, 10_000):
        for k in range(2, 10_000):
            x = k
            y = i
            step = 0
            resto = x % y
            step += 1
            while resto > 0:
                x = y
                y = resto
                resto = x % y
                step += 1
            steps.append(step)
    print(max(steps))


number_of_steps_in_euclidean_algorithm()
