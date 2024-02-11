s = open('source/24-17.txt').readline()
c = 1
mc = 0
a = 0
s = s.split('A')
for i in range(len(s)):
    if 'E' in s[i]:
        c = 0
        mc = max(mc, c)
    else:
        a += 1
        c += 1 + len(s[i])
        mc = max(mc, c)
        if a == 700:
            c = 1
            a = 0
print(mc)