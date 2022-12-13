from time import time
start = time()


def collatz_conjecture():
    """
    This function treat about de Collatz Conjecture.
    :return:
    """
    a, b, cont, lc = 35603679, 47792812, 0, []
    for num in range(a, b + 1):
        while num != 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = 3 * num + 1
            cont += 1
        lc.append(cont)
        cont = 0
    return print(max(lc))


collatz_conjecture()

end = time()
print(f"{end - start:.2f}s")
