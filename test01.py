s = "123421"
b = 3
cont = 0
print(s[b - 2], end="")
print(s[b - 1],)
print(s[b], end="")
print(s[b + 1])
print(s[b - 2:b + 2])
"""
while len(s) > 0 or cont == len(s):
    if s[b - 1] == s[b]:
        s = s.replace(s[b - 1:b + 1], "")
        b -= 1
    print(len(s))
    cont += 1
"""