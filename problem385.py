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
    t = int(input())
    n_step = list(map(int, input().split(" ")))
    steps, n, resposta, respostas = 0, 0, [], []
    x, y = 1, 1
    while x <= 200:
        while y <= 200:
            if x < y:
                break
            else:
                a, b = x, y
                while b != 0:
                    a, b = b, a % b
                    steps += 1
                    if steps == n_step[n]:
                        print(x, y)
                        resposta.append(x)
                        resposta.append(y)
                        respostas.append(resposta)
                        resposta = []
                        print(x, y, steps, n_step)
                        x, y, steps = 1, 1, 0
                        n += 1
                    if steps > n_step[n] or steps < n_step[n]:
                        steps = 0
                        x += 1
                        if x == 200:
                            x = 1
                            y += 1
                        break


number_of_steps_in_euclidean_algorithm()
