s = open('source/24_58327.txt').readline()
c = 1
mc = 0
for i in range(len(s) - 1):
    if int(s[i]) >= int(s[i + 1]):
        c += 1
    else:
        mc = max(mc, c)
        c = 1
print(mc)