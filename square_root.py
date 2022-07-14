def main():
    from csv import reader
    """
    Many mathematical problems are solved in programming not precisely, but
    approximately, by several computations of the result, each of which is
    more and more close to the goal.

    Let us practice the method of approximate calculation of the square root
    with the following approach:

    Let us search for square root r of the given value X.
    Use some arbitrary value, say r = 1 as the first approximation (surely
    it is too rough).
    For proper square root the equation r = X / r should hold.
    So let us calculate d = X / r (it would not be equal to r since r is not
    precise root). 
    And take average between r and d as the new approximation.
    E.g. overall formula of the calculation step is (here := is an assignment):

          r  +  X / r
    r := -------------
               2
    Refer to Square Root Approximation article for more details on the Heron's
    Method.

    So we are given values X for which to perform calculations and number of steps
    N to perform. Use r = 1 at the beginning, and output resulting approximation
    (after N steps).

    Input data will give the number of test-cases in first line.
    Next lines will contain test-cases themselves, each containing the value X
    for which square root should be calculated and N - the number of calculation steps.

    Answer should contain calculated approximations for each case, separated by space.

    Example:

    input data:
    3
    150 0
    5 1
    10 3

    answer:
    1 3 3.196

    Results should have precision of 1e-7 = 0.0000001 or better!
    """
    with open('square_root.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        data = [row for row in reader_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            data[k][i] = int(data[k][i])
    for k in range(0, len(data)):
        s, r = 0, 1
        x = data[k][0]
        n = data[k][1]
        while s < n:
            d = x / r
            r = (r + d) / 2
            s += 1
        print(f'{r:.7f}', end=' ')


if __name__ == '__main__':
    main()
