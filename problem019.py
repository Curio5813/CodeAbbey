from csv import reader


def justBrackets():
    """
    This function open a .csv file and return a list of strings of brackets.
    :return:
    """
    arq = open("problem019.csv")
    l1 = reader(arq)
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(l1[i][k])
    return l2


def matchingBrackets(l2):
    """
    This function take a parameter given by the function above and
    return the number "1" if brackets matching or "0" otherwise.
    :param l2:
    :return:
    """
    l3 = []
    for k in range(0, len(l2)):
        expressao = l2[k]
        for i in range(len(expressao)):
            ch = expressao[i]
            if ch == '{' or ch == '[' or ch == '(' or ch == '<':
                l3.append(ch)
            elif ch == '}' or ch == ']' or ch == ')' or ch == '>':
                if len(l3) != 0:
                    chx = str(l3.pop())
                    if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '(') or \
                            (ch == '>' and chx != '<'):
                        break
        if len(l3) != 0:
            print(0, end=" ")
        elif len(l3) == 0:
            print(1, end=" ")
        l3 = []


matchingBrackets(justBrackets())
