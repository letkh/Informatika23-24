f = open('source/26-25.txt')
m, n = map(int, f.readline().split())
data = []
for i in range(n):
    x, y = map(int, f.readline().split())
    data.append([x, y])
data.sort(key=lambda x: (x[0],x[1]), reverse=True)
res = []
for i in range(m):
    res.append(data.pop(0))
print(res)
print()
print(data)
print(res[-1])
print(data[0])
