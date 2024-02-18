with open('source/17.txt') as f:
    s = [int(x) for x in f]
    mel = max([x for x in s if 10000 <= x <= 99999 and x % 10 == 3])
    triples = []
    for i in range(len(s)-2):
        x, y, z = s[i], s[i+1], s[i+2]
        if (abs(x) % 10 == 3 or abs(y) % 10 == 3 or abs(z) % 10 == 3) and (x + y + z <= mel):
            triples.append(x + y + z)

print(len(triples), max(triples))