def main():
    from csv import reader
    from datetime import datetime
    """
    Dealing with remainders may cause heavy headache to novice programmers. Let us write a
    simple program which has this operation for its core to study integer division better.
    At the same time we'll have some practice in handing dates - which sometimes gives headache
    even to experienced coders.

    In arithmetic, the remainder (or modulus) is the amount "left over" after performing the
    division of two integers which do not divide evenly (from Wiki). This task will provide
    further practice with modulo operation.

    Suppose, we are given two timestamps - for example, when the train or ferry boat starts its
    travel and when it finishes. This may look like:

    start: May 3, 17:08:30
    end  : May 8, 12:54:15
    and we are curious to know, how much time (in days, hours, minutes and seconds) is spent in
    traveling (perhaps, to choose faster variant). How this could be achieved?

    One of the easiest way is:

    convert both timestamps to big numbers, representing seconds from the beginning of the month
    (or year, or century);
    calculate their difference - i.e. travel time in seconds;
    convert this difference back to days, hours, minutes and seconds.
    First operation could be performed by multiplying minutes by 60 and hours by 60*60 etc. and
    summing all values up.
    The third operation should be performed on contrary by several divisions with keeping remainders.

    In this task we are given several pair of timestamps. We suppose that both dates in the pair
    are always in the same month, so only number of day will be given. We want to calculate
    difference between timestamps in each pair.

    Input data: the first line contains number of test-cases, other lines contain test-cases
    themselves. Each test-case contains 8 numbers, 4 for each timestamp: day1 hour1 min1 sec1
    day2 hour2 min2 sec2 (second timestamp will always be later than first).
    Answer: for each test-case you are to output difference as following
    (days hours minutes seconds) - please note brackets - separated by spaces.

    Example:

    input data:
    3
    1 0 0 0 2 3 4 5
    5 3 23 22 24 4 20 45
    8 4 6 47 9 11 51 13

    answer:
    (1 3 4 5) (19 0 57 23) (1 7 44 26)
    """
    l1, l2, time1, time2 = [], [], [], []
    with open('modulo_and_time_difference.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        times = [row for row in reader_csv]
    for k in range(0, len(times)):
        for i in range(0, len(times[k])):
            l1.append(int(times[k][i]))
        l2.append(l1)
        l1 = []
    for k in range(0, len(l2)):
        if l2[k][0] == 0:
            l2[k][0] = 1
            l2[k][4] += 1
        time1 = datetime(year=2021, month=10, day=l2[k][0], hour=l2[k][1], minute=l2[k][2], second=l2[k][3])
        time2 = datetime(year=2021, month=10, day=l2[k][4], hour=l2[k][5], minute=l2[k][6], second=l2[k][7])
        delta = time2 - time1
        dias = delta.days
        segundos = delta.seconds
        horas = segundos // 3600
        segundos -= horas * 3600
        minutos = segundos // 60
        segundos -= minutos * 60
        print(f'({dias} {horas} {minutos} {segundos})', end=' ')


if __name__ == '__main__':
    main()
