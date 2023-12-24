with open('source/17-25.txt') as f:
    s = [int(x) for x in f]
    mx = 0
    mx1 = 0
    k = 0
    for i in range(len(s)):
        if s[i] % 1000 == 100:
            mx = max(mx, s[i])
    for i in range(len(s) - 2):
        x,y,z = s[i], s[i+1], s[i+2]
        if ( ((len(str(x)) == 3) + (len(str(y)) == 3) + (len(str(z)) == 3) == 2) and ((x + y + z) <= mx) ):
            k += 1
            mx1 = max(mx1, x + y + z)
print(k, mx1)