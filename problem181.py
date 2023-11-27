from csv import reader
from math import prod, sqrt


def reverse_polish_notation():
    """
    Most of us get used to using infix math notation while writing
    arithmetic expressions, like this:

    2 * 4 + 9 / 3

    Meanwhile in programming the concept of postfix notation is often
    exploited. This form (often called also Reverse Polish Notation)
    was used in many programmable calculators and in some languages
    (e.g. Forth) to simplify processing. Moreover one of the popular
    ways of parsing and executing of infix notation is via conversion
    to postfix one.

    Some languages (like LISP) also use prefix notation which gives
    similar advantages.

    Let us see few examples. Operation on two values is simply written
    after them:

    2 4 *           multiply 2 by 4

    9 3 /           divide 9 by 3

    8 3 +           sum 8 and 3

    More complex expression:

    5 2 3 * +       5 + 2 * 3

    5 2 + 3 *       (5 + 2) * 3

    You see, Polish notation does not need brackets (parentheses) since the
    order of operation is always determined.

    Processing of RPN
    Simple way to evaluate expression in RPN is by using stack and the following
    algorithm:

    loop through all tokens of the expression;
    if the next token is a value, it is pushed onto stack;
    if it is operation, then a pair of values are popped from stack, operation is
    done on them and result is pushed back;
    after the whole expression is processed, stack contains a single value which
    is the result of evaluation.
    It is also easy to extend these rules for using unary operations - for them
    only one value should be popped from the stack instead of two. So for example
    formula for root of quadratic equation:

    (sqrt(b * b - 4 * a * c) - b) / (2 * a)
    Could be written as:

    b b * 4 a * c * - sqrt b - 2 a * /

    Your Goal
    You are given a long expression in postfix notation, which contains integer
    values and operations:

    add and sub for + and -;
    mul, div and mod for *, / and remainder;
    sqrt for taking square root.
    You are to calculate the result.

    Input data contains the expression, which may consist of few hundreds tokens.
    Answer should contain single integer value - the result.
    :return:
    """
    arq = open("problem181.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    stack = []
    for i in range(0, len(l1)):
        if l1[i] != "add" and l1[i] != "sub" and l1[i] != "mul" and l1[i] != "div" \
                and l1[i] != "sqrt" and l1[i] != "mod":
            l1[i] = int(l1[i])
    i = 0
    while i in range(0, len(l1)):
        if l1[i] == "add":
            soma = sum(stack)
            stack = [soma]
        if l1[i] == "sub":
            n = i
            sub = stack[0]
            print(sub)
            print(stack)
            while type(l1[i]) is not str:
                sub = stack[n] - l1[n]
                n -= 1
            stack = [sub]
            print(sub)
            print(stack)
        if l1[i] == "mul":
            mult = prod(stack)
            stack = [mult]
        if l1[i] == "div":
            divid = stack[0] / l1[i - 1]
            stack = [divid]
        if l1[i] == "mod":
            modulo = stack[0] % l1[i - 1]
            stack = [modulo]
        if l1[i] == "sqrt":
            raiz = sqrt(stack[0])
            stack = [raiz]
        if l1[i] != "add" and l1[i] != "sub" and l1[i] != "mul" and l1[i] != "div" \
                and l1[i] != "sqrt" and l1[i] != "mod":
            stack.append(l1[i])
        i += 1
    print(stack)


reverse_polish_notation()
