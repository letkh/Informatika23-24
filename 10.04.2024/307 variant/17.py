s = [int(x) for x in open('source/17-38.txt')]
res = []
mel = max([x for x in s if abs(x) % 100 == 72])
for i in range(len(s)-2):
    x, y, z = s[i], s[i+1], s[i+2]
    if len(str(abs(x + y + z))) == 5 and (x + y + z) ** 2 < mel ** 2:
        res.append(x + y + z)
print(len(res), max(res))