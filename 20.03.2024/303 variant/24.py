s = open('source/24.txt').readline()
s = s.split('AB')
ms = 0
for i in range(len(s) - 21):
    ms = max(ms, sum([len(s[j]) for j in range(i, i + 22)]))

print(ms + 44)