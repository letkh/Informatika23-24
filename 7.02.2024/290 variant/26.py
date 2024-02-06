f = open('source/26-8.txt')
n = int(f.readline())
a = []
for i in range(n):
    str = f.readline().split()
    a.append([int(str[0]), int(str[1])])
b = []
a.sort()
start = a[0][0]
end = a[0][1]
for i in range(1, len(a)):
    if a[i][1] > end and a[i][0] <= end:
        end = a[i][1]
    elif a[i][0] >= start and a[i][1] <= end:
        continue
    else:
        b.append([start, end])
        start = a[i][0]
        end = a[i][1]
b.append([start, end])
print('B:', b)