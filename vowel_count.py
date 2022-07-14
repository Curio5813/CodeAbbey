def main():
    """
    This is a simple problem to get introduced to string processing. We will be given
    several lines of text - and for each of them we want to know the number of vowels
    (i.e. letters a, o, u, i, e, y). Note: that y is regarded as vowel for purpose of
    this task.

    Though simple, this technic is important in cipher-breaking approaches. For example
    refer to Caesar Cipher Cracker problem.

    Input data contain number of test-cases in the first line.
    Then the specified number of lines follows each representing one test-case.
    Lines consist only of lowercase English (Latin) letters and spaces.

    Answer should contain the number of vowels in each line, separated by spaces.

    Example:

    input data:
    4
    abracadabra
    pear tree
    o a kak ushakov lil vo kashu kakao
    my pyx

    answer:
    5 4 13 2
    """
    cont, vowel = 0, []
    with open('vowel_count.txt') as arquivo:
        data = [row for row in arquivo.readlines()]
    for k in range(0, len(data)):
        data[k] = data[k].replace('\n', '')
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            if data[k][i] in 'aeiouy':
                cont += 1
        vowel.append(cont)
        cont = 0
    print(*vowel)


if __name__ == '__main__':
    main()
