with open('source/17.txt') as f:
    s = [int(x) for x in f]
    res = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            x, y = s[i], s[j]
            if abs(x - y) % 2 == 0 and (x % 31 == 0 or y % 31 == 0):
                res.append(x + y)
print(len(res), max(res))