P = list(range(56, 80))
Q = list(range(63, 86))
A = []
for x in range(100):
    if ((not((x in P) <= (x in Q))) <= ((x not in Q) <= (x in A))) == False:
        A.append(x)
print(A)