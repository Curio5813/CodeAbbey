def find_3_numbers():
    """
    You are given a positive integer N and must find 3 positive integers X, Y and Z
    which satisfy all of the following conditions.

    The 3 numbers X, Y and Z are all different and are all greater than 1.
    The products X*Y, X*Z and Y*Z are all divisors of N.
    The product X*Y*Z is a multiple of N.
    For example, if N = 100 we find that X = 2, Y = 5 and Z = 10 satisfies these 3
    conditions. The products X*Y, X*Z and Y*Z are 10, 20 and 50 respectively. All of
    these are divisors of N = 100. The product X*Y*Z = 2*5*10 = 100 = 1 x 100. So this
    is a multiple of N as required.

    If we consider N = 35 we soon find that there is no combination of integers X, Y
    and Z which satisfy the requirements.

    For each solution you must give the 3 values of X, Y and Z in ascending size order,
    separated by single spaces. If there is no solution for a particular value of N,
    you indicate this with a single 0 in place of the 3 values for X, Y and Z.

    Input/Output description: The first line of the input data will contain a single
    integer M, the number of different values of N to consider. M lines will follow.
    Each line contains a single value of N. Find the corresponding values of X, Y and Z
    (in ascending order) or report 0 if there is no solution. Combine all answers into a
    single string, separated by spaces.
    :return:
    """
    temp, asw, flag = [], [], 0
    m = int(input())
    for i in range(m):
        n = int(input())
        for j in range(2, n):
            for k in range(2, n):
                for p in range(2, n):
                    if j != k and k != p and j != p and n % (j * k) == 0 and n % (j * p) == 0 and n % (k * p) == 0 and (j * k * p) % n == 0:
                        temp.append(j)
                        temp.append(k)
                        temp.append(p)
                        asw.append(temp)
                        temp = []
                        flag = 1
                if flag == 1:
                    break
            if flag == 1:
                flag = 0
                break
        else:
            temp.append(0)
            asw.append(temp)
            temp = []
    for i in range(0, len(asw)):
        print(*asw[i], end=" ")


find_3_numbers()
