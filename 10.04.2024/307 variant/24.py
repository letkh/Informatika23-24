s = open('source/24-23.txt').readline()
c = 0
mc = 0
for i in range(len(s) - 1):
    if s[i] + s[i+1] not in 'AABBCCDDEE' and s[i] in 'ABCDE':
        c += 1
    else:
        mc = max(c, mc)
        c = 0
print(mc)