s = open('source/24-18.txt').readline()
a = 0
c = 1
mc = 0
for i in range(len(s)):
    if s[i] == 'A':
        a += 1
        c += 1
        if a > 3:
            c = 0
            a = 0
    else:
        c += 1
        mc = max(mc, c)
print(mc)