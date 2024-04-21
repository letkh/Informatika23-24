s = open('source/24.txt').readline()
c = 0
mc = 0
for i in s:
    if c == 0 and i == '0':
        continue
    elif i in '012345':
        c += 1
        mc = max(mc, c)
    else:
        c = 0
print(mc)