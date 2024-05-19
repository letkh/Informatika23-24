s = open('source/24.txt').readline()
c = 1
mc = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        mc = max(c, mc)
        c = 1
    else:
        c += 1
print(mc)
