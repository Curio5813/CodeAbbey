from csv import reader


def sumOfDigits():
    """
    This function return the sum of digits given in a list
    with three values with the first multipled by second and
    the result of mutiplicantion is add to third number into list.
    :return:
    """
    arq = open("problem011.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    l2, l3, soma, somas, l4, l5 = [], [], 0, [], [], [],
    for i in range(0, len(l1)):           # This loop take the values in a list of strings
        for k in range(0, len(l1[i])):    # and convert it to integer.
            l1[i][k] = int(l1[i][k])
            l2.append(l1[i][k])
        l3.append(l2)
        l2 = []
    for i in range(0, len(l3)):           # This loop make the operations wih the terms and
        for k in range(0, len(l3[i])):    # put this in a lits.
            mult = l3[i][0] * l3[i][1]
            soma = mult + l3[i][2]
        somas.append(soma)
    for i in range(0, len(somas)):        # This loop sum all digit that used to make a number
        while somas[i] > 0:
            c = somas[i] % 10
            l4.append(c)
            somas[i] //= 10
        l5.append(sum(l4))
        l4 = []
    return print(*l5)


sumOfDigits()
