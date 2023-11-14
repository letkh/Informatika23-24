with open('source/17-18.txt') as f:
    s = [int(x) for x in f]
    mx = 0
    k = 0
    for i in range(len(s)):
        if s[i] % 4 == 0 and s[i] % 5 != 0 and s[i] % 8 != 0 and s[i] % 31 != 0 and s[i] % 41 != 0:
            k += 1
            mx = max(mx, s[i])
print(k, mx)