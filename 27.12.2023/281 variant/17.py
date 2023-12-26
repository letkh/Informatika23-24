with open('source/17-26.txt') as f:
    s = [int(x) for x in f]
    mx = 0
    mx1 = 0
    k = 0
    for i in range(len(s)):
        if s[i] % 100 == 17:
            mx = max(mx, s[i])
    for i in range(len(s) - 2):
        x,y,z = s[i], s[i+1], s[i+2]
        if ( ((len(str(x)) == 4) + (len(str(y)) == 4) + (len(str(z)) == 4)) == 2 and (x % 5 == 0 or y % 5 == 0 or z % 5 == 0) and (x + y + z > mx)):
            k += 1
            mx1 = max(mx1, x + y + z)
print(k, mx1)