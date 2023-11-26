with open("source/17.txt") as f:
    s = [int(x) for x in f]
    mx = 0
    c = 0
    mx1 = 0
    for i in range(len(s)):
        if len(str(s[i])) == 3 and s[i] % 10 == 4:
            mx = max(mx, s[i])
    for i in range(len(s) - 1):
        x, y = s[i], s[i+1]
        if ((x % 10 == 3 + y % 10 == 3) == 1) and ((x + y) / mx != 0):
            c += 1
            mx1 = max(mx1, x + y)

print(c, mx1)