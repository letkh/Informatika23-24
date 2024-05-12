s = [int(x) for x in open('source/17-40.txt')]
res = []
for i in range(len(s)-1):
    x, y = s[i], s[i+1]
    if x + y >= 50 and x >= 0 and y >= 0:
        res.append(x * y)
print(len(res), min(res))