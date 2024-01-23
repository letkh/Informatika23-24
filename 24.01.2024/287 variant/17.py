with open('source/17-31.txt') as f:
    a = []
    s = [int(x) for x in f]
    sr = [x for x in s if x % 4 == 0]
    mel = min(s)
    sr = sum(sr) / len(sr)
    for i in range(len(s)-1):
        x,y = s[i], s[i+1]
        if ((x % mel == 0) or (y % mel == 0)) and (x + y < sr):
            a.append(x + y)
print(len(a), max(a))