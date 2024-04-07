f = open('source/26-14.txt')
n = int(f.readline())
data = []
last = 0
for e in f:
    start, end = map(int, e.split())
    data.append([end, start])
data.sort()
count = []
z = 0
for i in range(n):
    if z == 0 or z <= data[i][1]:
        z = data[i][0]
        count.append(data[i])
        last = i
del count[-1]
z = count[-1][0]
for i in range(last + 1, n):
    if z <= data[i][1]:
        count.append(data[i])
print(len(count), count[-1][0] - count[-1][1])