import math

f = open('source/26-19.txt')
n, m = map(int, f.readline().split())
data = []
for i in range(n):
    data.append(int(f.readline()))
data.sort()
res = data[:m]
res1 = data[:m]
print(sum(res))
print(0.8 * sum(res))
while sum(res1) > (0.8 * sum(res)):
    res1.pop()
    if sum(res1[:-1]) > (0.8 * sum(res)):
        res1.pop()
    else:
        for i in range(len(res1), -1):
            if sum(res1) - res[i] > (0.8 * sum(res)):
                res1.pop(i)
                break

print(sum(res1))