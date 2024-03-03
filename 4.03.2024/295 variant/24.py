s = open('source/24-20.txt').readline()
c = 0
mc = 0
i = 0
while i < len(s) - 1:
    if s[i] + s[i+1] == 'XY':
        c += 1
        mc = max(mc, c)
        i += 2
    elif s[i] + s[i+1] == 'ZY' and s[i-2] + s[i-1] != 'XY' or c == 0:
        c += 1
        mc = max(mc, c)
        i += 2
    else:
        i += 1
        c = 0
print(mc)
