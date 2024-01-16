with open('source/27-A-8.txt') as file:
    n = int(file.readline())
    a = [int(s) for s in file]
    k = 0
    for i in range(n):
        for j in range(i, n):
            d = 0
            for k in range(i, j + 1):
                if a[k] > 0:
                    d += 1
                if a[k] < 0:
                    d -= 1
            if d == 0:
                k += 1
    print(k)