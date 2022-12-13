ARR_STR1 = ["1 2",
            "1 2 3",
            "2 3 4",
            "2 4 6 8 10",
            "7 11 19"]


def fool_day(strs):
    total = 0
    for i in strs:
        total += i * i
    return(total)


for lst in ARR_STR1:
    num = list(map(int, lst.split()))
    print(fool_day(num), end=" ")
