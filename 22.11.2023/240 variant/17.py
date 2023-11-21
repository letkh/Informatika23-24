with open('source/17-20.txt') as f:
    s = [int(x) for x in f]
    mn = min(s)
    mx = 0
    k = 0
    for i in range(len(s) - 1):
        x,y = s[i], s[i+1]
        if x % 117 == mn or y % 117 == mn:
            k += 1
            mx = max(x +y, mx)

print(k, mx)