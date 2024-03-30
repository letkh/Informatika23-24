with open('source/17.txt') as f:
    s = [int(x) for x in f]
    mel = min([x for x in s if abs(x) % 10 == 3 if len(str(abs(x))) == 4])
    res = []
    for i in range(len(s)-2):
        x,y,z = s[i],s[i+1],s[i+2]
        if ((abs(x) % 10 == 3) + (abs(y) % 10 == 3) + (abs(z) % 10 == 3) <= 2) and ((x + y + z) >= mel):
            res.append(x + y + z)
print(len(res), max(res))