def main():
    from collections import Counter
    """
    From this problem we will learn a popular programming trick used in many variants
    of statistic calculations.

    Imagine that some forester is trying to count pines, firs and birches on the some
    section of wood. He can go through this section three times, counting only pines
    on first pass, only firs on the second and only birches on the third.

    Traduzido:
    Imagine que alguns engenheiros florestais estejam tentando contar pinheiros, abetos e
    bétulas em alguma seção de madeira. Ele pode passar por esta seção três vezes, contando
    apenas pinheiros na primeira passagem, apenas abetos na segunda e por útilo, só bétulas.

    More efficient way is to make only one pass through wood and for each tree add a dot
    to one of tree pages in his notebook - the first page for pines, next for firs and
    last for birches. That is the idea of counting similar elements in the sequence using
    array of counters (instead of notebook).

    Here is an array of length M with numbers in the range 1 ... N, where N is less than or equal
    to 20. We are to go through it and count how many times each number is encountered.
    I.e. it is like Vowel Count task, but we need to maintain more than one counter. Be sure
    to use separate array for them, do not create a lot of separate variables, one for each counter.

    Input data contain M and N in the first line.
    The second (rather long) line will contain M numbers separated by spaces.

    Answer should contain exactly N values, separated by spaces. First should give amount of 1-s,
    second - amount of 2-s and so on.

    Example:

    data input:
    10 3
    3 2 1 2 3 1 1 1 1 3

    answer:
    5 2 3
    """
    values = []
    with open('array_counters.txt') as arquivo:
        data = [int(x) for x in arquivo.readline().split()]
    answer = dict(Counter(data))
    lista = sorted(answer.items())
    for k in range(0, len(lista)):
        values.append(lista[k][1])
    print(*values)


if __name__ == '__main__':
    main()
