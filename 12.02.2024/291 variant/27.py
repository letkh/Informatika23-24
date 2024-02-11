f = open('source/27_B.txt')
k = int(f.readline())
n = int(f.readline())
a = []
for i in range(n):
    val = int(f.readline())
    a.append([i, val])
max_multiply = 0
a.sort(key=lambda x: x[1], reverse=True)
b = [a[0][1]]
index = a[0][0]
for i in range(1, n):
    if abs(index - a[i][0]) >= k:
        b.append(a[i][1])
        index = a[i][0]
# print(a)
# print(b)
print(b[0] * b[1] * b[2])