def main():
    """
    Sum in Loop
    """
    with open('sum_in_loop.txt') as arquivo:
        lista = [int(x) for x in arquivo.readline().split()]
    print(sum(lista))


if __name__ == '__main__':
    main()
