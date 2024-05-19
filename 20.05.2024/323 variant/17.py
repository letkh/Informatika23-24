s = [int(x) for x in open('source/17.txt').read().split()]
res = []
for i in range(len(s)-1):
    if (s[i] > 700) or (s[i+1] > 700):
        res.append(s[i] ** 2 + s[i+1] ** 2)
print(len(res), max(res))
