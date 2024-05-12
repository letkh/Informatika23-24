s = open('source/24-25.txt').readline()
c = 1
mc = 0
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        c += 1
    else:
        mc = max(c, mc)
        c = 1
print(mc)