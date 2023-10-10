import math

for i in range(113000000, 114000000):
    a=[]
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0 and j % 2 == 0:
            a.append(j)
            b = i // j
            if j != b:
                a.append(b)

    if len(a)==3:
        a.sort()
        print(a[2])