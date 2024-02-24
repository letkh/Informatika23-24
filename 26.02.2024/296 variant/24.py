s = open('source/24.txt').readline()
s = s.replace('F', '&')
s = s.replace('G', '&')
s = s.replace('H', '&')
s = s.replace('E', '%')
s = s.replace('I', '%')
s = s.replace('&&','*')
s = s.replace('%%', '^')
c = 0
mc = 0
for i in range(len(s)):
    if s[i] == '*' or s[i] == '^':
        c += 1
    else:
        mc = max(c, mc)
        c = 0

print(mc)