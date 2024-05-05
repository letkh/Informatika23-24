s = [int(x) for x in open('source/17.txt')]
mel = min([x for x in s if x % 19 == 0])
a = []
for i in range(len(s) - 1):
    x, y = s[i], s[i+1]
    if x > mel or y > mel:
        a.append(x + y)
print(len(a), max(a))