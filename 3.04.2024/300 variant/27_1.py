f = open('source/27_A.txt')
k = int(f.readline())
n = int(f.readline())
data = []
for i in range(n):
    data.append([i, int(f.readline())])
data.sort(key=lambda x: x[0])
ms = 0
for i in range(n-k):
    fn = data[i][1]
    sn = max([data[x] for x in range(i + k, n)], key=lambda x: x[1])
    try:
        tn = max([data[x][1] for x in range(sn[0] + k, n)])
    except ValueError:
        continue
    ms = max(fn + sn[1] + tn, ms)
print(ms)