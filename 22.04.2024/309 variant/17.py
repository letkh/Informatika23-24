s = [int(x) for x in open('source/17.txt')]
res = []
for i in range(len(s)-2):
    x, y, z = s[i], s[i+1], s[i+2]
    if len(str(x)) != 3 and len(str(y)) != 3 and len(str(z)) != 3 and len(str(x + y + z)) == 5 and (x + y + z) % 21 == 0:
        res.append(x + y + z)
print(len(res), max(res))