s = open('source/24.txt').readline()
s = s.replace('ABC', '*')
a = 0
b = 0
c = 0
d = 0
for i in range(len(s)-1):
    if s[i] == '*':
        if s[i+1] == 'A':
            a += 1
        elif s[i+1] == 'B':
            b += 1
        elif s[i+1] == 'C':
            c += 1
        else:
            d += 1
print(a, b, c, d)