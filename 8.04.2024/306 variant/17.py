with open('source/17-37.txt') as f:
    s = [int(x) for x in f]
    mel = max([x for x in s if x % 100 == 17])
    res = []
    for i in range(len(s)-2):
        x,y,z = s[i], s[i+1], s[i+2]
        if ((len(str(x)) == 3) + (len(str(y)) == 3) + (len(str(z)) == 3) == 1) and x + y + z <= mel:
            res.append(x + y + z)
print(len(res), max(res))