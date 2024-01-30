f = open('source/24-14.txt')
s = f.readline()
k = 0
c = 1
mc = 0
for i in range(0, len(s)-1):
    if s[i] in 'AEIOUY' and s[i] < s[i+1]:
        k += 1
        c += 1
        mc = max(c, mc)
        if k == 2:
            c = 1
            k = 0
    elif s[i] not in 'AEIOUY' and s[i] < s[i + 1]:
        c += 1
        mc = max(c, mc)
    else:
        c = 1
        k = 0
print(mc)