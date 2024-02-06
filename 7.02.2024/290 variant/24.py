f = open('source/24-16.txt')
s = f.readline()
s = s.split('A')
k = 100000
for i in range(0,len(s)-500):
    c = 0
    for j in range(500):
        c += 1 + len(s[i + j])
    k = min(k, c)

print(k)