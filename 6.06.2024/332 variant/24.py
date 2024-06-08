s = open('source/24-33.txt').readline().replace('AB', '*')
n = []
m = 0
for i in range(len(s)):
    if s[i] == '*':
        n.append(i)

for i in range(len(n) - 599):
    m = max(m, n[i + 599] - n[i] + 1)

print(m)