for i in range(153222, 153271):
    k = 0
    for j in range(1, int((i // 2) ** 0.5) + 1):
        if (i - j * j) ** 0.5 % 1 == 0:
            p = j
            k += 1
    if k == 1:
        print(p, int((i - p * p) ** 0.5))