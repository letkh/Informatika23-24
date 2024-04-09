f = open("source/26-15.txt")
n, m = map(int, f.readline().split())
weight, allowed = [], []
for i in range(n + m):
    if i + 1 <= n:
        weight.append(int(f.readline().strip()))
    else:
        allowed.append(int(f.readline().strip()))
weight.sort(reverse=True)
allowed.sort(reverse=True)
res = []
# for load in weight:
#     if allowed[0] > load:
#         res.append(allowed.pop(0))
# print(len(res), res[0] - res[1])
for available in allowed:
    i = 0
    while i < len(weight):
        if available > weight[i]:
            res.append(weight.pop(0))
        i += 1
print(len(res), res[0] - res[1])