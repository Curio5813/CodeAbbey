from csv import reader


def girls_and_pigs():
    """
    Given a number of legs of women and pigs and the number of breasts
    this fucntion calculate and find the number of possible solutions
    of women and pigs. The numbers of breasts of pig is even and there
    is no limited.
    Input data will have the number of testcases in the first line.
    Next lines will contain a pair of values each - the amounts of legs
    and breasts - the first of them will always be smaller than the second.
    Answer should give the amount of solutions for each case.
    :return:
    """
    diff, woman_l, woman_b, n, pigs, pigs_l, pigs_b, solution, solutions = 2, 0, 0, 0, 0, 0, 0, 0, []
    arq = open("problem097.csv")
    l1 = reader(arq, delimiter="\n")
    l1 = list(l1)
    l2 = []
    # This snippet of the code transform strings in integer and put into a list
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(l1[i][k].split(" "))
    for i in range(0, len(l2)):
        for k in range(0, len(l2[i])):
            l2[i][k] = int(l2[i][k])
    # This snippet of the code calculate the number of possibel solutions of the amount
    # given of legs and breasts between girls and pigs.
    for i in range(0, len(l2)):
        for k in range(0, len(l2[i])):
            a = l2[i][0]
            legs = a
            b = l2[i][1]
            breasts = b
            while legs > 0:
                legs -= diff
                woman_l += 2
                woman_b += 2
                if legs == 0:
                    break
                breasts -= diff
                if legs % 4 == 0:
                    pigs = legs // 4
                    if breasts % pigs == 0 and (breasts // pigs) % 2 == 0:
                        solution += 1
                        # print(f"{pigs} {legs} {breasts} {woman_l} {woman_b} 'solution {solution}'")
            solutions.append(solution)
            woman_l, woman_b, solution = 0, 0, 0
            break
    print(*solutions)


girls_and_pigs()
