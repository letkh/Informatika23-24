def p(x, y, z):
    if (len(str(x)) == 5 or len(str(y)) == 5 or len(str(z)) == 5):
        if (len(str(x)) != 5 or len(str(y)) != 5 or len(str(z)) != 5):
            return True
    return False

def q(x, y, z):
    mod3 = 0
    mod5 = 0
    if x % 3 == 0:
        mod3 += 1
    if y % 3 == 0:
        mod3 += 1
    if z % 3 == 0:
        mod3 += 1
    if x % 5 == 0:
        mod5 += 1
    if y % 5 == 0:
        mod5 += 1
    if z % 5 == 0:
        mod5 += 1
    return mod3 > mod5


triples = []
with open('source/17.txt') as f:
    s = [int(x) for x in f]
    mel = max([int(x) for x in s if x % 1000 == 238])

    for i in range(len(s) - 2):
        x,y,z = s[i],s[i+1],s[i+2]
        if q(x,y,z) == True and p(x,y,z) == True and x + y + z > mel:
            triples.append(x+y+z)
print(len(triples), max(triples))