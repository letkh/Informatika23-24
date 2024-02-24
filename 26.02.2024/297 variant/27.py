f = open('source/27_A.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort(reverse=True)
ost = []
b = []
for i in range(n):
    if len(ost) == 4:
        break
    if a[i] % 4 in ost:
        continue
    b.append(a[i])
    ost.append(a[i]%4)
print(sum(b))