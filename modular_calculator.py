def main():
    from csv import reader
    """
    This task provides practice for core property of remainder taking operation in arithmetic -
    persisting of the remainder over addition and multiplication. This important property is
    often used for checking results of calculations, in competitive programming, in calculation
    checksums and especially for encryption.

    See Modular arithmetic for thorough explanations.

    We have a kind of long arithmetic calculation here, and we are asked about the result modulo
    some number (result % M in many languages).

    If you are curious why modular arithmetic is that important, you can see Public Key Cryptography
    Intro and RSA Cryptography exercises.

    Input data will have:
    Initial integer number in the first line;
    one or more lines describing operations, in form sign value where sign is either + or * and
    value is an integer; last line in the same form, but with sign % instead and number by which
    the result should be divided to get the remainder.
    
    Answer should give remainder of the result of all operations applied sequentially (starting with
    initial number) divided by the last number.

    If you have troubles with this problem, please feel free to type its name in the "Search" box
    in the top menu and find relevant topics at our forum - probably you will get enough enlightenment
    from there.

    Example:

    input data:
    5
    + 3
    * 7
    + 10
    * 2
    * 3
    + 1
    % 11
    answer:
    1

    In this case result after all operations applied sequentially is 397.

    All numbers will not exceed 10000 (though intermediate results could be very large).
    """
    oper = 0
    with open('modular_calculator.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        data = [row for row in reader_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            if k == 0:
                data[k][i] = int(data[k][i])
            else:
                data[k][1] = int(data[k][1])
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            if k == 0:
                oper = data[k][i]
            elif data[k][i] == '+':
                oper += data[k][i + 1]
            elif data[k][i] == '*':
                oper *= data[k][i + 1]
            elif data[k][i] == '%':
                oper %= data[k][i + 1]
    print(oper)


if __name__ == '__main__':
    main()
