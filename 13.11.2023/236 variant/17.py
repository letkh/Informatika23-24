with open('source/17.txt') as f:
    s = [int(x) for x in f]
    a = []
    mm = 0
    for i in range(len(s) - 1):
        if abs(s[i]) % 10 == 5 and abs(s[i+1]) % 10 == 5:
            a.append([s[i], s[i+1]])
            mm = max(mm, abs(s[i] - s[i + 1]))

print(len(a), mm)