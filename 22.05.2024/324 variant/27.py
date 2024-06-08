f = open('source/27_B-10.txt')
n, d = map(int, f.readline().split())
data = [[] for x in range(n)]
for i in range(n):
    num, res1, res2, res3 = map(int, f.readline().strip().split())
    if max(res1, res2, res3) - min(res1, res2, res3) <= d:
        data[num].extend([max(res1, res2, res3)])
data_sorted = [x for x in data if x != []]
res = []
for i in range(len(data_sorted)):
    res.append(max(data_sorted[i]))
print(res)
print(max(res))