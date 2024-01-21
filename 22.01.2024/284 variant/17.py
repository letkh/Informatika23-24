with open('source/17-30.txt') as f:
    s = [int(x) for x in f]
    mel = max([x for x in s if str(x)[:1] == '8'])
    group = []
    for i in range(len(s) - 2):
        x, y, z = s[i], s[i+1], s[i+2]
        if ((str(abs(x))[:1] == '6') + (str(abs(y))[:1] == '6') + (str(abs(z))[:1] == '6') <= 1) and ((x + y + z) >= mel):
            group.append(x + y + z)

print(len(group), min(group))
