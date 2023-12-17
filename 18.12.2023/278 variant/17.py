with open('source/17-24.txt') as f:
    s = [int(x) for x in f]
    mn = 100000000
    mx = 0
    k = 0
    for i in range(len(s)):
        if s[i] % 100 == 11:
            mn = min(mn, s[i])
    for i in range(len(s) - 1):
        x,y = s[i], s[i+1]
        if ( (len(str(x)) != 3 or len(str(y)) != 3) and ((x + y) % mn == 0)):
            k += 1
            mx = max(mx, x + y)
print(k, mx)