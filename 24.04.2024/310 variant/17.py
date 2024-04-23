s = [int(x) for x in open('source/17.txt')]
a = []
for i in range(len(s)):
    if str(s[i]).count('6') >= 1:
        a.append(s[i])
print(len(a), min(a))