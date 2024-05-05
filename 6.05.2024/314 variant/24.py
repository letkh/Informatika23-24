s = open('source/24.txt').readline()
c = 1
mc = 0
for i in range(len(s)-1):
    if s[i].isdigit() != s[i+1].isdigit():
        c += 1
    else:
        mc = max(mc, c)
        c = 1
print(mc)