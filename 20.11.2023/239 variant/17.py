with open('source/17-19.txt') as f:
    s = [int(x) for x in f]
    mn = min(s)
    mn1 = 10000
    k = 0
    for i in range(len(s) - 1):
        x, y = s[i], s[i + 1]
        if x % 111 == mn or y % 111 == mn:
            k += 1
            mn1 = min(mn1, x + y)

print(k, mn1)