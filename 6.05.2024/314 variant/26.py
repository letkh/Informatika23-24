f = open('source/26.txt')
n = int(f.readline())
a = sorted([int(x) for x in f], reverse=True)
res = [a[0]]
for i in range(1, n):
    if abs(res[-1] - a[i]) >= 8:
        res.append(a[i])
print(len(res), min(res))