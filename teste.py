a, b, l1 = 12345, 10, []
while a > 0:
    c = a % b
    l1.append(c)
    a //= 10
print(l1)

