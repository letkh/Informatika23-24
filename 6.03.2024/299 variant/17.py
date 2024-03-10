with open('source/17-36.txt') as f:
    s = [int(x) for x in f]
    a = []
    mel = max([x for x in s if abs(x) % 17 == 0])
    for i in range(len(s)-1):
        if s[i] + s[i+1] > mel:
            a.append(s[i] + s[i+1])
    print(len(a), max(a))