def main():
    """
    There are two widespread systems of measuring temperature - Celsius and Fahrenheit.
    First is quite popular in Europe and second is well in use in United States for example.

    By Celsius scale water freezes at 0 degrees and boils at 100 degrees.
    By Fahrenheit water freezes at 32 degrees and boils at 212 degrees. You may learn more from
    wikipedia on Fahrenheit.
    Use these two points for conversion of other temperatures.

    You are to write program to convert degrees of Fahrenheit to Celsius.

    Input data contains N+1 values, first of them is N itself (Note that you should not try to convert it).
    Answer should contain exactly N results, rounded to nearest integer and separated by spaces.

    Example:

    data:
    5 495 353 168 -39 22
    answer:
    257 178 76 -39 -6
    """
    celsius = []
    with open('fahrenheit_to_celsius.txt') as arquivo:
        data = [int(x) for x in arquivo.readline().split()]
    for k in range(0, len(data)):
        celsius.append(round((data[k] - 32) * (5/9)))
    print(*celsius)


if __name__ == '__main__':
    main()
