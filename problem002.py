from csv import reader


def sumInLoop():
    """
    This function calculate de sum of values within in a list
    given.
    :return:
    """
    arq = open("problem002.csv")
    lsum = reader(arq, delimiter=" ")
    lsum = list(lsum)
    soma = 0
    for i in range(0, len(lsum)):
        for k in range(0, len(lsum[i])):
            soma += int(lsum[i][k])
    return print(soma)


sumInLoop()
print("")
print("It's all folks!")
