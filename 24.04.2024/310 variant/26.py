file = open('source/26.txt')
first_line = file.readline().split()
d = int(first_line[0])
n = int(first_line[1])
vs = [int(x) for x in file.readlines()]

vs.sort()
k = 0
fix = 0
for i in range(len(vs)):
    if d - vs[i] >= 0:
        d -= vs[i]
        k += 1
    else:
        fix = vs[i-1]
        break

img_k = 0
for i in range(k, len(vs)):
    if vs[i]-fix <= d:
        img_k += 1
    else:
        break

print(k, n - k - img_k)