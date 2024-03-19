s = open('source/24.txt').readline()
s = s.split('AB')
ms = 10 ** 8
for i in range(len(s) - 20):
    ms = min(ms, sum([len(s[j]) for j in range(i, i + 20)]))

print(ms + 42)