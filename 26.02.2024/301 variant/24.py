s = open('source/24.txt').readline()

u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
c = 1
mc = 0
for i in range(len(s)):
    if s[i] == 'U':
        u += 1
    if s[i] == 'V':
        v += 1
    if s[i] == 'W':
        w += 1
    if s[i] == 'X':
        x += 1
    if s[i] == 'Y':
        y += 1
    if s[i] == 'Z':
        z += 1
    c += 1
    if u > 100 or v > 100 or w > 100 or x > 100 or y > 100 or z > 100:
        mc = max(c, mc)
        c = 0
print(mc)