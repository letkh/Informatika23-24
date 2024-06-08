s = [int(x) for x in open('source/17-42.txt')]
res = []
for i in range(len(s)):
    if s[i] % 5 == 0 and s[i] % 7 == 0 and s[i] % 2 != 0 and s[i] % 11 != 0 and s[i] % 91 != 0:
        res.append(s[i])
print(min(res), len(res))