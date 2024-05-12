file = open('source/27_B-8.txt')
n = int(file.readline())
a = file.readlines()
ms = 0
deltas = []
for i in range(n):
    ms += max([int(x) for x in a[i].split()])
    deltas.append(max([int(x) for x in a[i].split()])-min([int(x) for x in a[i].split()]))
if ms % 41 == 0:
    ms -= abs(min(deltas))

print(ms)