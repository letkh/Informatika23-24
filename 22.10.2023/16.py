f = open('1_17.txt')
s = [int(x) for x in f]
k = 0
maxd = 0
for i in range(len(s)):
    if abs(s[i]) % 100 == 17:
        maxd = max(maxd, s[i])
for i in range(len(s) - 2):
    c = 0
    l = [s[i], s[i+1], s[i +2]]
    for x in l:
        if 99 < abs(x) < 1000:
            c += 1
    if c == 1 and sum(l) < maxd:
        k += 1
print(k)