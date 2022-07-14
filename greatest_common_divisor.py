def main():
    from csv import reader
    from math import gcd
    """
    It looks like none of beginner's courses on programming avoids practicing Euclid's
    algorithm for calculation of the greatest common divisor of two numbers.

    Greatest Common Divisor or GCD of a and b is such an integer value c that both of a, b
    are divisible by it (e.g. leave no remainder) - and also c is the largest possible. For
    example gcd(20, 35) = 5 and gcd(13, 28) = 1. Euclid's algorithm is quite simple - we keep
    on subtracting smaller value (of a and b) from larger - and repeat this operation until
    values become equal - this last value will be gcd. For speeding up the process we can
    use modulo operation instead of subtraction.

    For example:

    20      35      - subtract first from second
    20      15      - subtract second from first
    5       15      - now subtract first from second twice
    5       5       - and here is GCD

    Least Common Multiple (or LCM) of a and b is such an integer d that it is divisible by
    both of them (and is the smallest of all possible). It can be found with the following rule:

    lcm(a, b) = a * b / gcd(a, b)

    The task
    Input data contain number of test-cases in the first line.
    Then lines with test-cases follow, each containing two numbers - for A and B.
    Answer should contain GCD and LCM for each pair, surrounded by brackets and separated by
    spaces, for example:

    input data:
    2
    2 3
    4 10

    answer:
    (1 6) (2 20)
    """
    lista, datas, greatest, least = [], [], [], []
    with open('greatest_common_divisor.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        data = [row for row in reader_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            lista.append(int(data[k][i]))
        datas.append(lista)
        lista = []
    for k in range(0, len(datas)):
        greatest.append(gcd(datas[k][0], datas[k][1]))
        least.append(int((datas[k][0] * datas[k][1]) / gcd(datas[k][0], datas[k][1])))
    for k in range(0, len(greatest)):
        print(f'({greatest[k]} {least[k]})', end=' ')


if __name__ == '__main__':
    main()
