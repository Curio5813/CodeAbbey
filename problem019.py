from csv import reader


def justBrackets():
    """
    This function open a .csv file and return a list of strings of brackets.
    :return:
    """
    arq = open("problem019.csv")
    l1 = reader(arq)
    l1 = list(l1)
    l2, l3 = "", []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            for m in range(0, len(l1[i][k])):
                if l1[i][k][m] in "()[]{}<>":
                    l2 += l1[i][k][m]
        l3.append(l2)
        l2 = ""
    return l3


def matchingBrackets(l3):
    """
    This function take a parameter given by the function above and
    return the number "1" if brackets matching or "0" otherwise.
    :param l3:
    :return:
    """
    stack = []
    for i in range(0, len(l3)):
        if i in ["(", "{", "[", "<"]:
            # Put the elements in the stack
            stack.append(i)
        else:
            # If current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_i = stack.pop()
            if current_i == '(':
                if i != ")":
                    return True
            if current_i == '{':
                if i != "}":
                    return True
            if current_i == '[':
                if i != "]":
                    return True
    # Check Empty Stack
    if stack:
        return print(0)
    return print(1)


if matchingBrackets(justBrackets()) is True:
    print(1)
elif matchingBrackets(justBrackets()) is False:
    print(0)


matchingBrackets(justBrackets())
