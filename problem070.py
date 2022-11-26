def linearCongruentialGenerator():
    """
    This function generate a pseudo-random number by obey
    the follow rule:

            Xnext = (A * Xcur + C) % M

    and returns the n-th member.
    :param l3:
    :return:
    """
    a, c, m, xc, l1 = 445, 700001, 2097152, 99658, []
    for i in range(6):
        # This is the formula of Linear Congruential Generator
        nex = (a * xc + c) % m
        # This updating the value of nex
        xc = nex
        l1.append(nex)
    print(l1)
    return l1


def funnyWordsGenerator(l1):
    """
    This function take the parameters give by the functions above
    and return the words you generated separated by space.
    :return:
    """
    con = "bcdfghjklmnprstvwxz"
    vow = "aeiou"
    word, i, idx1, idx2 = "", 0, 0, 0
    while len(word) <= 6:
        if i >= len(l1) - 1:
            break
        idx1 = l1[i] % 19
        word += con[idx1]
        idx2 = l1[i + 1] % 5
        word += vow[idx2]
    return print(word)


funnyWordsGenerator(linearCongruentialGenerator())
