with open('source/17 (4).txt') as f:
    s = [int(x) for x in f]
    mn = 10000
    c = 0
    mx = 0
    for i in range(len(s)):
        if s[i] % 25 == 0:
            mn = min(mn, s[i])
    for i in range(len(s) - 2):
        x, y, z = s[i], s[i+1], s[i+2]
        if ( ((len(str(x)) == 2) + (len(str(y)) == 2) + (len(str(z)) == 2) == 1) and (x + y + z < mn) ):
            c += 1
            mx = max(mx, x+y+z)
print(c, mx)