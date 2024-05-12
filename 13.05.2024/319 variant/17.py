s = [int(x) for x in open('source/17.txt')]
res = []
for i in range(len(s) - 1):
    x,y = s[i], s[i+1]
    if len(str(x)) != 3 and len(str(y)) != 3 and len(str(x + y)) == 4 and (x + y) % 7 == 0:
        res.append(x + y)
print(len(res), min(res))