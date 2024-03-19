import math

f = open('source/27_A.txt')
n = int(f.readline())
data = []
left = 0
right = 0
res = []
for i in range(n):
    a, b = map(int, f.readline().split())
    data.append([a, math.ceil(b / 15)])

tmp = 0
for i in range(1, n):
    tmp += (data[i][0] - data[0][0]) * data[i][1]
    right += data[i][1]
res.append(tmp)
for i in range(1, n):
    right -= data[i][1]
    left += data[i-1][1]
    res.append(res[i-1] - right*(data[i][0] - data[i-1][0]) + left*(data[i][0] - data[i-1][0]) - data[i][1]*(data[i][0] - data[i-1][0]))
print(min(res))