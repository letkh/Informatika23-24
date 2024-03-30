f = open('source/27_A.txt')
k = int(f.readline())
n = int(f.readline())
data = []
for i in range(n):
    data.append([i, int(f.readline())])
data.sort(reverse=True, key=lambda x: x[1])
print(data)
res = [data[0]]
for i in range(n - 1):
    if len(res) == 2:
        if (res[0][0] - data[i][0]) >= k and abs(res[-1][0] - data[i][0]) >= k:
            res.append(data[i])
            break
    elif abs(res[-1][0] - data[i][0]) >= k:
        res.append(data[i])
print(res)
print(sum([res[i][1] for i in range(3)]))
