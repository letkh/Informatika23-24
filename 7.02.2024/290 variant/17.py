def f(x):
    return 1000 <= abs(x) < 10000


s = [int(x) for x in open('source/17-34.txt')]
mel = max(x for x in s if abs(x) % 100 == 90)
a = []
for i in range(2, len(s)):
    if f(s[i - 2]) + f(s[i - 1]) + f(s[i]) > 0:
        if sum(s[i - 2: i + 1]) > mel:
            a.append(sum(s[i - 2: i + 1]))
print(len(a), min(a))
