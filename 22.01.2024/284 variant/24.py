dig = '0123456789'
f = open('source/24-12.txt')
s = f.readline()
c = 0
mc = 0
for i in range(0, len(s) - 1):
    if (s[i] in dig) + (s[i+1] in dig) == 1:
        c += 1
        mc = max(c, mc)
    else:
        c = 0
print(mc + 1)
