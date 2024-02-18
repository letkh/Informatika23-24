s = open('source/24.txt').readline()
c = 0
mc = 0
for i in range(len(s)-1):
    if s[i] in 'RSQ':
        if s[i] + s[i+1] in 'QRSQ':
            c += 1
            mc = max(c, mc)
        else:
            c = 1
    else:
        c = 0
print(mc)