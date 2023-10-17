f = open('source/27_A-1.txt')

n = int(f.readline())
d = 10001
sum = 0

for i in range(n):
    a = f.readline().split()
    x, y = int(a[0]), int(a[1])

    if x > y:
        sum = sum + x
    else:
        sum = sum + y

    if (abs(x - y) < d) and (abs(x - y) % 4 != 0):
        d = abs(x - y)

if sum % 4 != 0:
    print(sum)
else:
    print(sum - d)