from csv import reader


def expressionsWithBrackets():
    """
    This function open a .csv file and return a list of strings with brackets.
    :return:
    """
    arq = open("problem019.csv")
    l1 = reader(arq)
    l1 = list(l1)
    l2 = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l2.append(l1[i][k])
    print(l2)
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
        for i in expressao:
            ch = i
            if ch == '{' or ch == '[' or ch == '(' or ch == '<':
                # Stacking the data
                l3.append(ch)
            elif ch == '}' or ch == ']' or ch == ')' or ch == '>':
                if len(l3) != 0:
                    # Unstack the data
                    chx = str(l3.pop(-1))
                    if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '(') or \
                            (ch == '>' and chx != '<'):
                        # To force the error
                        l3.append(chx)
                        break
                elif len(l3) == 0:
                    if ch == '}' or ch == ']' or ')' or ch == '>':
                        # To force the error
                        l3.append(ch)
                        break
        if len(l3) != 0:
            print(0, end=" ")
        elif len(l3) == 0:
            print(1, end=" ")
        l3 = []


matchingBrackets(expressionsWithBrackets())
