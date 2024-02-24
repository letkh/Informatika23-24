f = open('source/27-A.txt')
n = int(f.readline())
a = ([int(x) for x in f])
a.sort(reverse=True)
b = []
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (a[i] + a[j] + a[k]) % 102 == 0:
                b.append(a[i] + a[j] + a[k])
print(max(b))
