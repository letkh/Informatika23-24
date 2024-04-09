import math

f = open('source/27A-1.txt')
n, m = map(int, f.readline().split())
data = []
left = 0
right = 0
res = []
for i in range(n):
    a, b = map(int, f.readline().split())
    data.append([a, math.ceil(b / 30)])

tmp = 0
for i in range(1, n):
    tmp += (data[i][0] - data[0][0]) * data[i][1]
    right += data[i][1]
res.append(tmp)
for i in range(1, n):
    right -= data[i][1]
    left += data[i-1][1]
    res.append(res[i-1] - right*(data[i][0] - data[i-1][0]) + left*(data[i][0] - data[i-1][0]) - data[i][1]*(data[i][0] - data[i-1][0]))
print(max(res))