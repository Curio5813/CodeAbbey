from time import time
start = time()


def collatz_conjecture():
    """
    This function treat about de Collatz Conjecture.
    :return:
    """
    a, b, cont1, l1 = 1492, 2018, 0, []
    for num in range(a, b + 1):
        while num != 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = 3 * num + 1
            cont1 += 1
        l1.append(cont1)
        cont1 = 0
    return print(max(l1))


collatz_conjecture()

end = time()
print(f"{end - start:.2f}s")
