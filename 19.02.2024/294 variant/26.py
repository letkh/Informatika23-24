f = open('source/26.txt')
s, n = f.readline().split()
a = [int(x) for x in f.readlines()]
a.sort()
b = []
for i in range(int(n)):
    if sum(b) <= int(s):
        b.append(a[i])
    else:
        break
b.pop()
b.pop()
for i in range(len(a) - 1, -1, -1):
    if sum(b) + a[i] <= int(s):
        b.append(a[i])
        break
# print(b)
print(len(b), max(b))
# print(sum(b))
