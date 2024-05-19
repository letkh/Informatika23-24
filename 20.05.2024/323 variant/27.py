s = open("source/27_B.txt").readlines()
n = int(s[0])
sm = 0
d = 10**6
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    sm += max(x, y)
    if abs(x - y) % 43 != 0:
        d = min(d, abs(x - y))
if sm % 43 != 0:
    print(sm)
else:
    print(sm - d)