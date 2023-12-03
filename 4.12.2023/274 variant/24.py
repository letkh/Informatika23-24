f = open('source/24 (2).txt')
s = f.readline()
l = 0
mini = 10000
pos = []
for i in range(len(s)):
    if s[i] == 'A':
        pos.append(i)
for i in range(2025, len(pos)):
    l = pos[i] - pos[i-101] - 1
    mini = min(mini, l)
print(mini)