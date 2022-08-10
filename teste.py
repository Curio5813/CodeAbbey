l1 = [3, 1, 4, 1, 5, 9]
soma, res, mod = 0, 113, 10000007
for i in range(0, len(l1)):
    soma += l1[i]
    soma *= res
    soma %= mod
print(soma)
