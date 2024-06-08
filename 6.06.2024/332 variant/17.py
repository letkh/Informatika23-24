s = [int(x) for x in open('source/17-48.txt')]
tmp = [x for x in s if abs(x) % 100 == 74]
res = []
for i in range(len(s) - 2):
    x, y, z = s[i], s[i + 1], s[i + 2]
    if ((len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) + (len(str(abs(z))) == 4) >= 2) and x ** 2 + y ** 2 + z ** 2 <= max(tmp) ** 2 + min(tmp) ** 2:
        res.append(x + y + z)
print(len(res), max(res))