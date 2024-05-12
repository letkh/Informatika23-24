f = open('source/26-17.txt')
s, n = map(int, f.readline().split())
data = [int(x) for x in f]
data.sort()
res = [data[0]]
i = 1
while i < n:
    if sum(res) + data[i] <= s:
        res.append(data[i])
        i += 1
    else:
        break
res.pop()
print(data)
for i in range(n-1, -1, -1):
    if sum(res) + data[i] <= s:
        res.append(data[i])
print(len(res), max(res))