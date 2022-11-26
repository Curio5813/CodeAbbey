def brainFibo():
    """
    This function print a sequence of numbers similar the operation
    to make a fibonacci sequence but the two initial numbers different
    are different that put in the sequence in
    your own order.
    :return:
    """
    k = int(input())
    a = int(input())
    b = int(input())
    p = a + b
    for i in range(k):
        a = b
        b = p
        p = a + b
        print(b)


brainFibo()
