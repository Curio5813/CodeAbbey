def main():
    from csv import reader
    from decimal import Decimal
    """
    John and Mary founded J&M publishing house and bought two old printers to equip it.
    
    Now they have their first commercial deal - to print a document consisting of N pages.
    
    It appears that printers work at different speed. One produces a page in X seconds 
    and other does it in Y seconds.
    
    So now company founders are curious about minimum time they can spend on printing the 
    whole document with two printers.
    
    Input data contains number of test cases in the first line.
    Then test-cases will follow, each in separate line.
    
    Each testcase contains three integer values - X Y N, where N will not exceed 1,000,000,000.
    Answer should contain minumum printing times for each of testcases, separated by spaces.
    
    Example:
    
    input data:
    2
    1 1 5
    3 5 4
    
    answer:
    3 9
    """
    rule, times, printer, printers = 0, [], [], []
    with open('two_printers.csv') as arquivo:
        reader_csv = reader(arquivo, delimiter=' ')
        data = [row for row in reader_csv]
    for k in range(0, len(data)):
        for i in range(0, len(data[k])):
            printer.append(int(data[k][i]))
        printers.append(printer)
        printer = []
    for k in range(0, len(printers)):
        rule = int(printers[k][2] / ((1 / printers[k][0]) + (1 / printers[k][1])))
        aprox = int(round((printers[k][0] * printers[k][1]) / (printers[k][0] + printers[k][1]) + 0.1))
        answer = rule + aprox
        times.append(answer)
    print(*times)


if __name__ == '__main__':
    main()

# 172344092 241405272 147872448 158515409 113713119 87055355 34765120 245534814 250980843
# 253948566 401933760 27067818 385569495 83468520 107143918 106487600 227647144 377653236

# 162268041 241405233 147872448 158275619 113708363 87055354 34712499 245457976 250980243
# 253947811 401918114 27067771 385569493 83468519 107142210 106487586 227647144 377120534

"""
50177836 43086023 7
132 72 5181678
12 18 20537840
937961 334440 642
24312 101439 5798
5 2 60938748
943606 66856 556
3360666 1996218 196
6973 3961 99356
20209 10051 37832
74848 87029 9988
241 114 349751
3 4 224915538
9 1 92742799
3122 19303 39869
206 400 783149
8 4 85367679
1482923 1724444 473
"""
