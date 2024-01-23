f = open('source/24-13.txt')
s = f.readline()
c = 0
mc = 0
a = 0
for i in range(len(s)):
    if s[i] == 'A':
        a += 1
        c += 1
        if a >= 2:
            c = 0
            a = 0
    else:
        c += 1
        mc = max(c, mc)

print(mc)