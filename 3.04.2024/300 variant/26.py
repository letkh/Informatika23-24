f = open('source/26.txt')
n = int(f.readline())
data = []
for i in range(n):
    line = f.readline().split()
    data.append([int(line[0]), int(line[1]), int(line[1]) - int(line[0])])
data.sort()
# print(data)
res = [data[0]]
for i in range(n):
    if res[-1][2] > data[i][2] and res[-1][1] > data[i][1]:
        res.pop()
        res.append(data[i])
    if res[-1][1] < data[i][0]:
        res.append(data[i])
res.pop()
res.append(data[-1])
print(len(res), res[-1][1])